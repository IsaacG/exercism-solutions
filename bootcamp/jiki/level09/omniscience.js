// Return the direction we will face if we rotate in a given direction.
function rotated with current, rotation do
  if rotation == "ahead" do
    return current
  else if rotation == "right" do
    return [-current[2], current[1]]
  else if rotation == "left" do
    return [current[2], -current[1]]
  end
end

// Return the next position we would move into if we rotated a certain way then moved forward.
function next_position with state, rotation do
  set direction to rotated(state["direction"], rotation)
  return [state["position"][1] + direction[1], state["position"][2] + direction[2]]
end

/// Return the square at a specific position.
function get_square with state, position do
  return state["squares"][position[2]][position[1]]
end

// Return if a specific position can be stepped on/moved into.
function can_step_on with state, position do
  set square to get_square(state, position)
  return not square.is_wall and square.contents != "🔥" and  square.contents != "💩"
end

// Return if you can turn in a given direction.
function can_turn with state, rotation do
  set pos to next_position(state, rotation)
  if pos[1] < 1 or pos[1] > state["max_x"] or pos[2] < 1 or pos[2] > state["max_y"] do
    return false
  end
  return can_step_on(state, pos)
end

// Move forward.
function do_move with state do
  move()
  change state["position"] to next_position(state, "ahead")
  return state
end

// Turn in a given direction.
function do_turn with state, rotation do
  if rotation == "left" do
    turn_left()
  else do
    turn_right()
  end
  change state["direction"] to rotated(state["direction"], rotation)
  return state
end

// Make progress towards the exit.
function progress with state do
  if can_turn(state, "left") do
    change state to do_turn(state, "left")  
  else if can_turn(state, "ahead") do
  else if can_turn(state, "right") do
    change state to do_turn(state, "right")
  else do
    change state to do_turn(state, "right")
    change state to do_turn(state, "right")
  end
  return do_move(state)
end

// Maybe add an emoji to the collection.
function pick_up with state do
  set square to get_square(state, state["position"])
  if square.contents == "" or square.is_finish or square.is_start do
    return state
  end

  if not my#has_key(state["collection"], square.contents) do
    change state["collection"][square.contents] to 0
  end
  change state["collection"][square.contents] to state["collection"][square.contents] + 1

  square.remove_emoji()
  return state
end

// Set the initial position and direction.
function set_start with state do
  for each row in state["squares"] indexed by y do
    for each square in row indexed by x do
      if square.is_start do
    	change state["position"] to [x, y]
      end
    end
  end
  for each direction in [[0, 1], [-1, 0], [1, 0], [0, -1]] do
    if can_step_on(state, [state["position"][1] + direction[1], state["position"][2] + direction[2]]) do
      change state["direction"] to direction
      break
    end
  end
  change state["max_x"] to my#length(state["squares"][1])
  change state["max_y"] to my#length(state["squares"])
  return state
end

// Solve the maze.
function solve_maze do
  set state to {"squares": get_initial_maze(), "collection": {}}
  change state to set_start(state)
  repeat_until_game_over do
    change state to progress(state)
    change state to pick_up(state)
  end
  announce_emojis(state["collection"])
end

solve_maze()
