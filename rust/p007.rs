fn prime(a: int) -> bool {
    if a < 2 {
        return false;
    }
    let mut i = 2;
    while i*i <= a {
        if a%i == 0 {
            return false;
        }
        i += 1;
    }
    return true;
}

fn main() {
    let mut count = 0;
    let mut i = 1;
    loop {
        if prime(i) {
            count += 1;
        }
        if count == 10001 {
            println(fmt!("%?",i));
            // output: 104743
            break;
        }
        i += 1;
    }
}
