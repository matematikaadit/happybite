import Data.List (group)

primes :: [Integer]
primes = 2 : filter ((==1) . length . primeFactors) [3,5..]

primeFactors   :: Integer -> [Integer]
primeFactors n = factor n primes
    where
      factor :: Integer -> [Integer] -> [Integer]
      factor n (p:ps)
          | p*p > n        = [n]
          | n `mod` p == 0 = p : factor (n `div` p) (p:ps)
          | otherwise      = factor n ps

triangleNumbers :: [Integer]
triangleNumbers = scanl1 (+) [1..]

nDivisors :: Integer -> Int
nDivisors n = product $ map ((+1) . length) (group (primeFactors n))

main :: IO ()
main = print . head . filter ((>500) . nDivisors) $ triangleNumbers
