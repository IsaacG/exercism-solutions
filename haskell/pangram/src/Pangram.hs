module Pangram (isPangram) where

import qualified Data.Char as C
import qualified Data.Set as S


isPangram :: String -> Bool
isPangram text = asciiLower `S.isSubsetOf` input
  where
    input = S.fromList $ map C.toLower text
    asciiLower = S.fromList ['a'..'z']

-- vim:ts=2:sw=2:expandtab
