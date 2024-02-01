from fpdf import FPDF

class Shirtificate():
    
    def __init__(self):
        self.name = input("Enter your name with surname : ").strip()
        self.n = 90-(len(self.name)*2)
        
    def make_pdf(self, pdf_format="A4", pdf_name="shirtificate.pdf"):
        self.pdf_format = pdf_format
        self.pdf_name = pdf_name
        pdf = FPDF(format = self.pdf_format)
        pdf.add_page()

        #for 1st font
        pdf.set_font("helvetica", "B", 45)
        pdf.set_xy(40,25)
        pdf.cell(0,10,txt="CS50 Shirtificate")

        #for t-shirt image
        pdf.image(r"shirtificate.png",x=10,y=70,w=190,h=200)

        #for 2nd font with name
        pdf.set_font("helvetica", "B", 20)
        pdf.set_text_color(255, 255, 255)
        pdf.set_xy(x=self.n,y=130)
        pdf.cell(0,10,txt=f"{self.name} took CS50")

        return pdf.output(f"{self.pdf_name}.pdf")
    
def main():
    shirtificate = Shirtificate()
    shirtificate.make_pdf("A4","shirtificate.pdf")
main()
