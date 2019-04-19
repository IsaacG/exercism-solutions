module Strain (keep, discard) where

-- Reimplement `filter`

discard :: (a -> Bool) -> [a] -> [a]
discard p xs = keep (\x -> not (p x)) xs

keep :: (a -> Bool) -> [a] -> [a]
keep p (x:xs)
  | p x = x:(keep p xs)
  | otherwise = keep p xs
keep _ [] = []
