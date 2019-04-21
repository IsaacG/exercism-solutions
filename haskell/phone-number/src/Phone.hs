module Phone (number) where

import Data.Char

-- Remove non-digits and strip leading country code.
clean :: String -> String
clean = (\ x -> if length x == 11 && head x == '1' then tail x else x ) . filter isDigit

valid :: String -> Bool
valid s
  | length s /= 10 = False
  | a == '0' || a == '1' = False
  | e == '0' || e == '1' = False
  | otherwise = True
  where
    a = head s
    e = s !! 3

number :: String -> Maybe String
number xs
  | valid c = Just c
  | otherwise = Nothing
  where c = clean xs
