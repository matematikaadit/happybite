package primes

func List(n int) []int {
	result := make([]int, 0, 65536)

	state := State(n)
	result = append(result, 2)

	for i := 3; i < n; i += 2 {
		if !state[i] {
			result = append(result, i)
		}
	}
	return result
}

func State(n int) []bool {
	state := make([]bool, n)
	state[0] = true
	state[1] = true
	for i := 4; i < n; i += 2 {
		state[i] = true
	}
	for i := 3; i*i < n; i += 2 {
		if !state[i] {
			for k := i * i; k < n; k += 2 * i {
				state[k] = true
			}
		}
	}

	return state
}

func Test(n int) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
