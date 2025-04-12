class TicTacToe do
  private property winning_combinations
  private property positions
  private property count
  private property moves

  constructor with moves do
    // Collect all possible rows of three; used later.
    set this.winning_combinations to [[[1, 1], [2, 2], [3, 3]], [[1, 3], [2, 2], [3, 1]]]
    for each i in [1, 2, 3] do
      change this.winning_combinations to push(this.winning_combinations, [[i, 1], [i, 2], [i, 3]])
      change this.winning_combinations to push(this.winning_combinations, [[1, i], [2, i], [3, i]])
    end

    set this.positions to [["", "", ""], ["", "", ""], ["", "", ""]]
    set this.count to 0
    set this.moves to moves
  end

  private method draw_board do
    // Setup. Draw the both. Initialize variables.
    rectangle(5, 5, 90, 90)
    line(5, 35, 95, 35)
    line(5, 65, 95, 65)
    line(35, 5, 35, 95)
    line(65, 5, 65, 95)
  end

  // Draw a player's move -- either a "X" or a "O".
  private method draw_move with y, x, count do
    if count % 2 == 1 do
      circle(20 + 30 * x, 20 + 30 * y, 10)
    else do
      line(10 + x * 30, 10 + y * 30, 30 + x * 30, 30 + y * 30)
      line(10 + x * 30, 30 + y * 30, 30 + x * 30, 10 + y * 30)
    end
  end

  // Check if there are three in a row. If there is, return the row.
  private method is_winner do
    for each row in this.winning_combinations do
      // Check the first position is not empty and that it matches the other two positions.
      if this.positions[row[1][1]][row[1][2]] != "" and this.positions[row[1][1]][row[1][2]] == this.positions[row[2][1]][row[2][2]] and this.positions[row[1][1]][row[1][2]] == this.positions[row[3][1]][row[3][2]] do
        return [true, row]
      end
    end
    return [false, []]
  end

  // Game over! Update the move colors and display the winner.
  private method game_over with important_moves, msg do
    set idx to 0
    repeat this.count times do
      change idx to idx + 1
      this.end_game_color(this.moves[idx][1], this.moves[idx][2], important_moves)
      this.draw_move(this.moves[idx][1] - 1, this.moves[idx][2] - 1, idx)
    end
    rectangle(0, 0, 100, 100)
    this.write_message(96, 79, 205, 0.85, msg)
    return 0
  end

  // Write a message on a given background color.
  private method write_message with r, g, b, a, msg do
    rectangle(0, 0, 100, 100)
    fill_color_rgba(r, g, b, a)
    write(msg)
  end
  
  // Set the stroke color used at the end of a game: purple for winning moves, light grey for others.
  private method end_game_color with x, y, important_moves do
    stroke_color_hex("light_grey")
    for each move in important_moves do
      if x == move[1] and y == move[2] do
        stroke_color_hex("purple")
        return
      end
    end
  end
  
  // Return if a given row has two in a row with the third position empty.
  private method near_win with row do
    set counts to [0, 0]
    set empty_count to 0
    set empty_position to 0
    set player to 0
    for each position in row do
      if this.positions[position[1]][position[2]] == "" do
        change empty_count to empty_count + 1
        change empty_position to position
      else do
        change counts[this.positions[position[1]][position[2]] + 1] to counts[this.positions[position[1]][position[2]] + 1] + 1
        change player to this.positions[position[1]][position[2]]
      end
    end
    // If the empty count is 1, the other counts are either [1, 1] or [0, 2] or [2, 0].
    if empty_count == 1 and counts[1] != 1 do
      return [true, player, empty_position]
    end
    return [false]
  end
  
  // Suggest the next move.
  private method ai do
    // this.positions, this.count % 2, this.winning_combinations
    set two_in_a_row to 0
    // Check if the current player can win. If not, check if the other player can win.
    for each offset in [0, 1] do
      for each row in this.winning_combinations do
        change two_in_a_row to this.near_win(row)
        if two_in_a_row[1] and two_in_a_row[2] == (this.count + offset) % 2 do
          return two_in_a_row[3]
        end
      end
    end
    // Neither player can win on the next turn. Pick any available position.
    for each row in this.winning_combinations do
      for each pos in row do
        if this.positions[pos[1]][pos[2]] == "" do
          return pos
        end
      end
    end
  end

  public method play do
    set won to []
    this.draw_board()
    for each move in this.moves do
      change this.count to this.count + 1
      // Set/check the move.
      if move == "?" do
        change move to this.ai()
        change this.moves[this.count] to move
      else if this.positions[move[1]][move[2]] != "" do
        this.write_message(200, 0, 0, 0.85, "Invalid move!")
        return 0
      end
      // Update the board.
      this.draw_move(move[1] - 1, move[2] - 1, this.count)
      change this.positions[move[1]][move[2]] to this.count % 2
      // Check for a winner.
      change won to this.is_winner()
      if won[1] do
        set msg to concatenate("The ", ["x", "o"][(this.count % 2) + 1], "'s won!")
        return this.game_over(won[2], msg)
      end
      if this.count == 9 do
        return this.game_over([], "The game was a draw!")
      end
    end
  end
end

// Play the game.
function run_game with moves do
  set game to new TicTacToe(moves)
  game.play()  
end
