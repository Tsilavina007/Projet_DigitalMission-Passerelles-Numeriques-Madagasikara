import qrcode

data = [
    "ADELAIDE SEHENOARISOA",
    "Angelico Razafindramisy",
    "ANJARA RAZAFINDRAVONY",
    "DIDIER RATOLOJANAHARY",
    "DIHARINIAINA RABEARIMANANA",
    "EDWINE ROJOVELONA",
    "ELISE RAZAFIMANANA",
    "ELIVETTE RAVAONIARISOA",
    "FENITRA ANDRIANAIVO",
    "FIDELICIA RASOAHERINIAINA",
    "FREDDY ANDRIAMANOHINIAINA",
    "JONATHAN SANDRINO",
    "JUDICAEL FAIBATO",
    "Julia KAMISY",
    "KEVIN RANDRIANARISON",
    "MIANTSA RAKOTONOELY",
    "NEKENA NYFANOMEZANTSOA",
    "ODAUPHIN JEAN-CRYS",
    "PASCALINE ZAFIMBITIANA",
    "PIERROT DJAONASY",
    "RADO ANDRIANTSOA",
    "TOKINIAINA RAHARIJAONA",
    "TSILAVINA ANDRIAMIHARISON",
    "TSIORY RABEARIVONY",
    "ZANATIANA ZOELINE"
]

# Création des QR codes pour chaque élément de la liste data
for i, item in enumerate(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(item)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(f"{item}.png")
