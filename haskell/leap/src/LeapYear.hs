module LeapYear (isLeapYear) where

isLeapYear :: Integer -> Bool
isLeapYear year
  | isDiv year 400 = True
  | isDiv year 100 = False
  | isDiv year 4 = True
  | otherwise = False
 where isDiv = (\x y -> (mod x y) == 0)
