fn primegen(n: uint) -> ~[uint] {
    let mut state: ~[bool] = std::vec::from_elem(n, true);
    state[0] = false;
    state[1] = false;
    let mut i = 2;
    while i*i < n {
        if state[i] {
            let mut k = i*i;
            while k < n {
                state[k] = false;
                k += i;
            }
        }
        i += 1;
    }
    let mut primes: ~[uint] = ~[];
    for i in range(0,n) {
        if state[i] {
            primes.push(i);
        }
    }
    primes
}

fn main() {
    let MAX = 2000000;
    let mut sum: u64 = 0;
    let primes = primegen(MAX);

    for i in primes.iter() {
        sum += *i as u64;
    }
    println!("{:u}", sum);
    // output: 142913828922
}
