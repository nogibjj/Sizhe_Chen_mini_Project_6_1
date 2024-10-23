use clap::Parser; // Import the Parser trait from clap

#[derive(Parser, Debug)]
#[command(version = "1.0", about = "Calculate the average of two numbers")]
struct Args {
    num1: i64,
    num2: i64,
}

// New function to calculate the average of two numbers
fn calculate_average(x: i64, y: i64) -> f64 {
    let sum = x + y;
    sum as f64 / 2.0
}

fn main() {
    let args = Args::parse(); // Parse the command-line arguments

    let result = calculate_average(args.num1, args.num2);
    println!("The average of num1 and num2 is: {}", result);
}
