main :: IO ()
main = print . sum $ primes 2000000

primes :: Integer -> [Integer]
primes m = 2 : sieve [3,5..m] where
    sieve (p:xs)
          | p*p > m   = p : xs
          | otherwise = p : sieve (xs `minus` [p*p, p*p+2*p..])

minus :: Ord a => [a] -> [a] -> [a]
minus (x:xs) (y:ys) = case (compare x y) of
           LT -> x : minus  xs   (y:ys)
           EQ ->     minus  xs      ys
           GT ->     minus (x:xs)   ys
minus xs      _     = xs
