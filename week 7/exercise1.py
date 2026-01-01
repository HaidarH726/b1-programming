# Product Pricing Manager
# Reads products from products.txt
# Applies discounts
# Writes pricing_report.txt
import logging

def calculate_discount(category, tier):
    # Category discounts (%)
    category_discounts = {
        "Electronics": 10,
        "Clothing": 15,
        "Books": 5,
        "Home": 12
    }

    # Tier discounts (%)
    tier_discounts = {
        "Premium": 5,
        "Standard": 0,
        "Budget": 2
    }

    # Get discounts safely (default 0 if not found)
    category_discount = category_discounts.get(category, 0)
    tier_discount = tier_discounts.get(tier, 0)

    return category_discount + tier_discount


def process_products(input_file, output_file):
    products = []
    total_discount = 0

    # -------- READ FILE --------
    try:
        with open(input_file, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) != 4:
                    continue  # skip bad lines

                name, price_str, category, tier = parts

                try:
                    base_price = float(price_str)
                except ValueError:
                    continue  # skip invalid prices

                discount_pct = calculate_discount(category, tier)
                discount_amount = base_price * (discount_pct / 100)
                final_price = base_price - discount_amount

                products.append(
                    (name, base_price, discount_pct, discount_amount, final_price)
                )

                total_discount += discount_pct

    except FileNotFoundError:
        print("Error: products.txt not found")
        return

    # -------- WRITE REPORT --------
    try:
        with open(output_file, "w") as file:
            file.write("PRODUCT PRICING REPORT\n")
            file.write("=" * 70 + "\n")
            file.write(
                f"{'Product':<25} {'Base':>10} {'Disc %':>10} "
                f"{'Disc $':>10} {'Final':>10}\n"
            )
            file.write("-" * 70 + "\n")

            for product in products:
                name, base, pct, disc_amt, final = product
                file.write(
                    f"{name:<25} "
                    f"${base:>9.2f} "
                    f"{pct:>9.1f}% "
                    f"${disc_amt:>9.2f} "
                    f"${final:>9.2f}\n"
                )

            file.write("=" * 70 + "\n")

    except PermissionError:
        print("Error: Cannot write pricing_report.txt")
        return

    # -------- PRINT SUMMARY --------
    if products:
        avg_discount = total_discount / len(products)
    else:
        avg_discount = 0

    print("\nProcessing complete!")
    print(f"Total products processed: {len(products)}")
    print(f"Average discount applied: {avg_discount:.2f}%")
    print("Report saved to pricing_report.txt")


# -------- RUN PROGRAM --------
if __name__ == "__main__":
    process_products("products.txt", "pricing_report.txt")
