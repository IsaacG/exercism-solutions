class Location do
  private property direction
  public property position

  constructor with position, direction do
    set this.position to position
    set this.direction to direction
  end

  private method rotated with rotation do
    if rotation == "ahead" do
      return [this.direction[1], this.direction[2]]
    else if rotation == "right" do
      return [-this.direction[2], this.direction[1]]
    else if rotation == "left" do
      return [this.direction[2], -this.direction[1]]
    else do
      return [-this.direction[1], -this.direction[2]]
    end
  end

  // Return the next position we would move into if we rotated a certain way then moved forward.
  public method next_position with rotation do
    set direction to this.rotated(rotation)
    return [this.position[1] + direction[1], this.position[2] + direction[2]]
  end

  // Turn in a given direction.
  public method turn with rotation do
    if rotation == "left" do
      turn_left()
    else if rotation == "right" do
      turn_right()
    else if rotation == "behind" do
      turn_right()
      turn_right()
    end
    change this.direction to this.rotated(rotation)
  end

  public method move do
    move()
    change this.position to this.next_position("ahead")
  end
end

class Maze do
  private property location
  private property collection
  private property squares
  private property max_x
  private property max_y

  constructor do
    set this.collection to {}
    set this.squares to get_initial_maze()
  
    // Set the initial position and direction.
    for each row in this.squares indexed by y do
      for each square in row indexed by x do
        if square.is_start do
        	set start_position to [x, y]
        end
      end
    end
    for each direction in [[0, 1], [-1, 0], [1, 0], [0, -1]] do
      if this.can_step_on([start_position[1] + direction[1], start_position[2] + direction[2]]) do
        set start_direction to direction
        break
      end
    end
    set this.location to new Location(start_position, start_direction)
    set this.max_x to my#length(this.squares[1])
    set this.max_y to my#length(this.squares)
  end

  // Return if a specific position can be stepped on/moved into.
  private method can_step_on with position do
    set square to this.squares[position[2]][position[1]]
    return not square.is_wall and square.contents != "🔥" and  square.contents != "💩"
  end

  // Return if you can turn in a given direction.
  private method can_turn with rotation do
    set pos to this.location.next_position(rotation)
    if pos[1] < 1 or pos[1] > this.max_x or pos[2] < 1 or pos[2] > this.max_y do
      return false
    end
    return this.can_step_on(pos)
  end

  // Make progress towards the exit.
  private method progress do
    for each direction in ["left", "ahead", "right", "behind"] do
      if this.can_turn(direction) do
        this.location.turn(direction)  
        break
      end
    end
    this.location.move()
  end
  
  // Maybe add an emoji to the collection.
  private method pick_up do
    set square to this.squares[this.location.position[2]][this.location.position[1]]
    if square.contents == "" or square.is_finish or square.is_start do
      return
    end
    change this.collection[square.contents] to my#get(this.collection, square.contents, 0) + 1
    square.remove_emoji()
  end

  // Solve the maze.
  public method solve do
    repeat_until_game_over do
      this.progress()
      this.pick_up()
    end
    announce_emojis(this.collection)
  end
end

set maze to new Maze()
maze.solve()
