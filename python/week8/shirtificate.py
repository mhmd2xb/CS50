from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 36)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C",
             new_x="LMARGIN", new_y="NEXT")

    shirt_w = 120
    shirt_h = 120
    x = (210 - shirt_w) / 2
    y = 50
    pdf.image("shirtificate.png", x=x, y=y, w=shirt_w, h=shirt_h)

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(y + 45)
    pdf.cell(0, 10, name, align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
