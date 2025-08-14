import argparse
import unicodedata
import string

SIGNOS = set(string.punctuation)

def quitar_acentos(texto: str) -> str:
    texto_normalizado = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in texto_normalizado if not unicodedata.combining(c))

def normalizar_texto(
    texto: str,
    sensible_mayus: bool = False,
    conservar_espacios: bool = False,
    conservar_signos: bool = False,
    quitar_acentos_flag: bool = True,
    forma_normalizacion: str = "NFC",
) -> str:
    try:
        texto = unicodedata.normalize(forma_normalizacion, texto)
    except Exception:
        texto = unicodedata.normalize("NFC", texto)
    if not sensible_mayus:
        texto = texto.casefold()
    if quitar_acentos_flag:
        texto = quitar_acentos(texto)
    if not conservar_espacios:
        texto = "".join(c for c in texto if not c.isspace())
    if not conservar_signos:
        texto = "".join(c for c in texto if c not in SIGNOS)
    return texto

def es_palindromo_basico(texto: str) -> bool:
    t = "".join(c for c in texto if not c.isspace()).casefold()
    return t == t[::-1]

def es_palindromo(
    texto: str,
    sensible_mayus: bool = False,
    conservar_espacios: bool = False,
    conservar_signos: bool = False,
    quitar_acentos_flag: bool = True,
    forma_normalizacion: str = "NFC",
) -> bool:
    t = normalizar_texto(
        texto,
        sensible_mayus=sensible_mayus,
        conservar_espacios=conservar_espacios,
        conservar_signos=conservar_signos,
        quitar_acentos_flag=quitar_acentos_flag,
        forma_normalizacion=forma_normalizacion,
    )
    return t == t[::-1]

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("texto")
    parser.add_argument("--sensible-mayus", action="store_true")
    parser.add_argument("--conservar-espacios", action="store_true")
    parser.add_argument("--conservar-signos", action="store_true")
    parser.add_argument("--no-quitar-acentos", action="store_true")
    parser.add_argument("--usar-basico", action="store_true")
    args = parser.parse_args(argv)
    if args.usar_basico:
        ok = es_palindromo_basico(args.texto)
    else:
        ok = es_palindromo(
            args.texto,
            sensible_mayus=args.sensible_mayus,
            conservar_espacios=args.conservar_espacios,
            conservar_signos=args.conservar_signos,
            quitar_acentos_flag=not args.no_quitar_acentos,
        )
    print("✅ Es palíndroma" if ok else "❌ No es palíndroma")
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
