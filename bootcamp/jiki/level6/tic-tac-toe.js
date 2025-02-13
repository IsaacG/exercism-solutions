// Draw a player's move -- either a "X" or a "O".
function draw_move with y, x, player_one do
  if player_one % 2 == 1 do
    circle(20 + 30 * x, 20 + 30 * y, 10)
  else do
    line(10 + x * 30, 10 + y * 30, 30 + x * 30, 30 + y * 30)
    line(10 + x * 30, 30 + y * 30, 30 + x * 30, 10 + y * 30)
  end
end

// Check if there are three in a row. If there is, return the row.
function is_winner with positions, rows do
  for each row in rows do
    // Check the first position is not empty and that it matches the other two positions.
    if positions[row[1][1]][row[1][2]] != "" and positions[row[1][1]][row[1][2]] == positions[row[2][1]][row[2][2]] and positions[row[1][1]][row[1][2]] == positions[row[3][1]][row[3][2]] do
      return [true, row]
    end
  end
  return [false]
end

// Write a message on a given background color.
function write_message with r, g, b, a, msg do
  rectangle(0, 0, 100, 100)
  fill_color_rgba(r, g, b, a)
  write(msg)
end

// Set the stroke color used at the end of a game: purple for winning moves, light grey for others.
function end_game_color with x, y, important_moves do
  stroke_color_hex("light_grey")
  for each move in important_moves do
    if x == move[1] and y == move[2] do
      stroke_color_hex("purple")
      return
    end
  end
end

// Game over! Update the move colors and display the winner.
function game_over with moves, important_moves, count, msg do
  set idx to 0
  repeat count times do
    change idx to idx + 1
    end_game_color(moves[idx][1], moves[idx][2], important_moves)
    draw_move(moves[idx][1] - 1, moves[idx][2] - 1, idx)
  end
  rectangle(0, 0, 100, 100)
  write_message(96, 79, 205, 0.85, msg)
  return 0
end

// Return if a given row has two in a row with the third position empty.
function near_win with positions, row do
  set counts to [0, 0]
  set empty_count to 0
  set empty_position to 0
  set player to 0
  for each position in row do
    if positions[position[1]][position[2]] == "" do
      change empty_count to empty_count + 1
      change empty_position to position
    else do
      change counts[positions[position[1]][position[2]] + 1] to counts[positions[position[1]][position[2]] + 1] + 1
      change player to positions[position[1]][position[2]]
    end
  end
  // If the empty count is 1, the other counts are either [1, 1] or [0, 2] or [2, 0].
  if empty_count == 1 and counts[1] != 1 do
    return [true, player, empty_position]
  end
  return [false]
end

// Suggest the next move.
function ai with positions, turn, rows do
  set two_in_a_row to 0
  // Check if the current player can win. If not, check if the other player can win.
  for each offset in [0, 1] do
    for each row in rows do
      change two_in_a_row to near_win(positions, row)
      if two_in_a_row[1] and two_in_a_row[2] == (turn + offset) % 2 do
        return two_in_a_row[3]
      end
    end
  end
  // Neither player can win on the next turn. Pick any available position.
  for each row in rows do
    for each pos in row do
      if positions[pos[1]][pos[2]] == "" do
        return pos
      end
    end
  end
end

// Play the game.
function run_game with moves do
  log moves
  // Collect all possible rows of three; used later.
  set rows to [[[1, 1], [2, 2], [3, 3]], [[1, 3], [2, 2], [3, 1]]]
  for each i in [1, 2, 3] do
    change rows to push(rows, [[i, 1], [i, 2], [i, 3]])
    change rows to push(rows, [[1, i], [2, i], [3, i]])
  end
  
  // Setup. Draw the both. Initialize variables.
  rectangle(5, 5, 90, 90)
  line(5, 35, 95, 35)
  line(5, 65, 95, 65)
  line(35, 5, 35, 95)
  line(65, 5, 65, 95)
  set positions to [["", "", ""], ["", "", ""], ["", "", ""]]
  set won to []

  set count to 0
  for each move in moves do
    change count to count + 1
    log move
    // Set/check the move.
    if move == "?" do
      change move to ai(positions, count % 2, rows)
      change moves[count] to move
    else if positions[move[1]][move[2]] != "" do
      write_message(200, 0, 0, 0.85, "Invalid move!")
      return 0
    end
    // Update the board.
    draw_move(move[1] - 1, move[2] - 1, count)
    change positions[move[1]][move[2]] to count % 2
    // Check for a winner.
    change won to is_winner(positions, rows)
    if won[1] do
      set msg to concatenate("The ", ["x", "o"][(count % 2) + 1], "'s won!")
      return game_over(moves, won[2], count, msg)
    end
    if count == 9 do
      return game_over(moves, [], count, "The game was a draw!")
    end
  end
end
