largestPrimeFactor :: Integer -> Integer
largestPrimeFactor n = recursiveLPF n 2
    where
      recursiveLPF num factor
          | n == 1                = 1
          | num == 1              = factor
          | num `mod` factor == 0 = recursiveLPF (num `div` factor) factor
          | num < factor * factor = num
          | otherwise             = recursiveLPF num (factor + 1)

main :: IO ()
main = do
    print $ largestPrimeFactor 600851475143
