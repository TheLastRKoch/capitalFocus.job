class ScraperService:

    def get_invoice_details(self, vendor):
        match command:
          case "BAC":
              print("Start processing "+vendor)
          case "WINK":
              print("Start processing "+vendor)
          case _:
              print("Start processing "+vendor)