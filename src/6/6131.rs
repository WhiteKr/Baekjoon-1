#![allow(non_snake_case)]

macro_rules! get_line {
    ( $( $t: ty ),+ ) => {
        {
            let mut line = String::new();

            std::io::stdin().read_line(&mut line).unwrap();

                let mut iter = line.split_whitespace();

            ( $( iter.next().unwrap().parse::<$t>().unwrap() ),+ )
        }
    }
}

fn main() {
    let N = get_line!(i32);
    let mut count = 0;

    for i in 1..=500 {
        for j in 1..=500 {
            if j * j == i * i + N {
                count += 1;
            }
        }
    }

    println!("{}", count);
}