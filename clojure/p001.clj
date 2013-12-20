(defn multiple-of-3-or-5 [x]
  (or (= (rem x 3) 0)
      (= (rem x 5) 0)))

(reduce +
  (filter
    multiple-of-3-or-5
    (range 1 1000)))