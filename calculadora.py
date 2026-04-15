#!/usr/bin/env python3
"""Calculadora simples de terminal."""


def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def ler_numero(prompt: str) -> float:
    while True:
        entrada = input(prompt).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido. Digite um número.")


def main() -> None:
    print("=== Calculadora Simples ===")
    print("Operações: +  -  *  /")

    while True:
        operacao = input("Escolha a operação (+, -, *, /) ou 'sair': ").strip().lower()

        if operacao == "sair":
            print("Até logo!")
            break

        if operacao not in {"+", "-", "*", "/"}:
            print("Operação inválida. Tente novamente.\n")
            continue

        numero1 = ler_numero("Digite o primeiro número: ")
        numero2 = ler_numero("Digite o segundo número: ")

        try:
            if operacao == "+":
                resultado = somar(numero1, numero2)
            elif operacao == "-":
                resultado = subtrair(numero1, numero2)
            elif operacao == "*":
                resultado = multiplicar(numero1, numero2)
            else:
                resultado = dividir(numero1, numero2)

            print(f"Resultado: {resultado}\n")
        except ZeroDivisionError as erro:
            print(f"Erro: {erro}\n")


if __name__ == "__main__":
    main()
