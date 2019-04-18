module LeapYear (isLeapYear) where

isLeapYear :: Integer -> Bool
isLeapYear year
  | isDiv 400 = True
  | isDiv 100 = False
  | isDiv 4 = True
  | otherwise = False
 where isDiv = (\div -> (mod year div) == 0)
