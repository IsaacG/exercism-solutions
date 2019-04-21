module Triangle (rows) where

-- Given one row, compute the next row.
-- Zip and add the row with itself, shifted by one, to get the middle elements.
-- Add the first/last element to either end (typically 1 and 1).
nextRow :: [Integer] -> [Integer]
nextRow xs = head xs:(zipWith (+) xs (tail xs) ++ [last xs])

rows :: Int -> [[Integer]]
rows x
  | x == 0 = []
  | x == 1 = [[1]]
  | otherwise = r ++ [nextRow . last $ r]
    where r = rows (x - 1)
