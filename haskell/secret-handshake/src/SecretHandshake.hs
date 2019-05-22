module SecretHandshake (handshake) where

import Data.Bits

construct :: Int -> [String]
construct n =
  map
    snd
    $ filter
      (testBit n . fst)
      $ zip [0..] actions
  where actions = ["wink", "double blink", "close your eyes", "jump"]

handshake :: Int -> [String]
handshake n
  | testBit n 4 = reverse $ construct n
  | otherwise   = construct n

-- vim:ts=2:sw=2:expandtab
