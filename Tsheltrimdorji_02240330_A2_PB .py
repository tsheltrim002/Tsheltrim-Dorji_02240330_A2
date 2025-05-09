class PokemonBinder:
    def __init__(self):
        self.cards = []  # Stores all Pokemon cards
        self.max_pokedex = 1025
        self.cards_per_page = 64
        self.grid_size = 8  # 8x8 grid
    
    def add_card(self, pokedex_num):
        """Add a card to the binder or show if it exists"""
        if pokedex_num in self.cards:
            page, row, col = self._calculate_position(pokedex_num)
            return f"Card already exists! Page {page}, Row {row}, Column {col}"
        else:
            self.cards.append(pokedex_num)
            self.cards.sort()  # Keep them in order
            page, row, col = self._calculate_position(pokedex_num)
            return f"Card added! Page {page}, Row {row}, Column {col}"
    
    def _calculate_position(self, pokedex_num):
        """Calculate page number and grid position"""
        page = ((pokedex_num - 1) // self.cards_per_page) + 1
        position_in_page = (pokedex_num - 1) % self.cards_per_page
        row = (position_in_page // self.grid_size) + 1
        col = (position_in_page % self.grid_size) + 1
        return page, row, col
    
    def reset(self):
        """Clear all cards from the binder"""
        self.cards = []
        return "Binder has been reset. All cards removed."
    
    def get_status(self):
        """Return current collection stats"""
        total = len(self.cards)
        percent = (total / self.max_pokedex) * 100
        return {
            'cards': sorted(self.cards),
            'total': total,
            'percent': f"{percent:.1f}%"
        }

def main():
    binder = PokemonBinder()
    
    while True:
        print("\nPokemon Card Binder Manager")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View binder status")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            try:
                num = int(input("Enter Pokedex number (1-1025): "))
                if 1 <= num <= 1025:
                    print(binder.add_card(num))
                else:
                    print("Please enter a number between 1-1025")
            except ValueError:
                print("That's not a valid number!")
        
        elif choice == "2":
            print("\nWARNING: This will delete ALL cards!")
            confirm = input("Type 'CONFIRM' to reset: ").upper()
            if confirm == "CONFIRM":
                print(binder.reset())
            else:
                print("Reset cancelled")
        
        elif choice == "3":
            status = binder.get_status()
            print("\nCurrent cards:", status['cards'])
            print("Total cards:", status['total'])
            print("Completion:", status['percent'])
        
        elif choice == "4":
            print(f"\nGoodbye! You collected {len(binder.cards)} cards.")
            break
        
        else:
            print("Please enter a number 1-4")

if __name__ == "__main__":
    print("Welcome to Pokemon Card Binder Manager!")
    main()