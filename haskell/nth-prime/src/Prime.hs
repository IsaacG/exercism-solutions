module Prime (nth) where

isDiv :: Int -> Int -> Bool
isDiv x y = (mod x y) == 0

-- Test if n is a prime number
isPrime :: Int -> Bool
isPrime n
  | n <= 1 = False
  | n == 2 = True
  | isDiv n 2 = False
  | otherwise = divLoop n (n-2)

-- Test for prime-ness by dividing by a candidate value
divLoop :: Int -> Int -> Bool
divLoop n m
  | m <= 2 = True
  | isDiv n m = False
  | otherwise = divLoop n (m-2)

primes :: [Int]
primes = filter isPrime [1,2..]

nth :: Int -> Maybe Integer
nth n
  | n < 1 = Nothing
  | otherwise = Just $ toInteger $ last $ take n primes
