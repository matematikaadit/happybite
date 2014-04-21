evenfib = [x | x <- takeWhile (<= 4000000) fibs, even x]
  where fibs = 1:1:zipWith (+) fibs (tail fibs)

main = do
  print $ sum evenfib
