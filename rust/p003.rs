fn main() {
	let mut	n: i64 = 600851475143;
	let mut	k: i64 = 2;
	let mut	last: i64 = k;
	while n > 1 {
		if n%k == 0 {
			last = k;
			while n%k == 0 {
				n /= k;
			}
		}
		k += 1;
	}
	println(last.to_str())
	// output: 6857
}

