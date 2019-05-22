module Hamming (distance) where

reduce :: Int -> (Char, Char) -> Int
reduce c (x, y) = if x == y then c else c + 1

distance :: String -> String -> Maybe Int
distance xs ys
  | length xs /= length ys = Nothing
  | otherwise = Just $ foldl reduce 0 $ zip xs ys


-- vim:ts=2:sw=2:expandtab
