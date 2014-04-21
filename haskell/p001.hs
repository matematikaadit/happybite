cond x = x `mod` 3 == 0 || x `mod` 5 == 0

main = do
  print $ sum [x | x <- [1..999], cond x]
