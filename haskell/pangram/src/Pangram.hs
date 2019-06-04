module Pangram (isPangram) where

import qualified Data.Char as C
import qualified Data.Set as S

foundAll :: S.Set Char -> String -> Bool
foundAll s (c:cs)
  | S.size s == 26 = True
  | otherwise      = foundAll (S.insert c s) cs
foundAll s []
  | S.size s == 26 = True
  | otherwise      = False


isPangram :: String -> Bool
isPangram text = foundAll S.empty lower_input
  where
    lower_input = map C.toLower $ filter C.isLetter text

-- vim:ts=2:sw=2:expandtab
