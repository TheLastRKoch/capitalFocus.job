from services.validator import Validator

def main():
    validator = Validator()

    # Example 1: Schema and Data
    schema1 = 
    data1 = {
        "addressee": "MARCELO CASTRO HENCHOZ",
        "sender": "SERGIO SEGURA VIDAL",
        "account": "*****6158",
        "date": "01-03-2026 15:41:01",
        "amount": "4.000,00",
        "description": "Anillos________",
        "reference": "2026030110283000877943114"
    }

    print("--- Validating Example 1 ---")
    is_valid, message = validator.validate_json(data1, schema1)
    print(f"Is valid: {is_valid}")
    print(f"Message: {message}")
    print()

    # Example 2: Schema and Data
    schema2 = {
        "type": "object",
        "properties": {
            "Comercio": {"type": "string"},
            "Ciudad y pais": {"type": "string"},
            "Fecha": {"type": "string"},
            "MASTER": {"type": "string"},
            "Autorizacion": {"type": "string"},
            "Referencia": {"type": "string"},
            "Tipo de Transaccion": {"type": "string"},
            "Monto": {"type": "string"}
        },
        "required": ["Comercio", "Ciudad y pais", "Fecha", "MASTER", "Autorizacion", "Referencia", "Tipo de Transaccion", "Monto"]
    }
    data2 = {
        "Comercio": "SERVICENTRO TROVA EL G",
        "Ciudad y pais": "CARTAGO, Costa Rica",
        "Fecha": "Mar 1, 2026, 20:05",
        "MASTER": "************1406",
        "Autorizacion": "019819",
        "Referencia": "95711481",
        "Tipo de Transaccion": "COMPRA",
        "Monto": "CRC 17,007.00"
    }

    print("--- Validating Example 2 ---")
    is_valid, message = validator.validate_json(data2, schema2)
    print(f"Is valid: {is_valid}")
    print(f"Message: {message}")
    print()
    
    # Example 3: Invalid Data
    data3 = {
        "addressee": "MARCELO CASTRO HENCHOZ",
        "sender": "SERGIO SEGURA VIDAL",
        "account": "*****6158",
        "date": "01-03-2026 15:41:01",
        "amount": "4.000,00",
        "description": "Anillos________",
    }

    print("--- Validating Example 3 (Invalid) ---")
    is_valid, message = validator.validate_json(data3, schema1)
    print(f"Is valid: {is_valid}")
    print(f"Message: {message}")
    print()


if __name__ == "__main__":
    main()
