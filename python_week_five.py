# Base class
class Superhero:
    def __init__(self, name, secret_identity, powers, weakness, energy_level=100):
        # Public attributes
        self.name = name
        self.powers = powers
        
        # Protected attributes (accessible to subclasses)
        self._secret_identity = secret_identity
        self._weakness = weakness
        
        # Private attributes
        self.__energy_level = energy_level
        self.__mission_count = 0
    
    # Public methods
    def use_power(self, power_name):
        if power_name in self.powers and self.__check_energy(10):
            self.__energy_level -= 10
            print(f"{self.name} uses {power_name}! ⚡ Energy level: {self.__energy_level}%")
            return True
        print(f"{self.name} cannot use {power_name} or is too tired!")
        return False
    
    def complete_mission(self, mission_difficulty):
        energy_cost = mission_difficulty * 15
        if self.__check_energy(energy_cost):
            self.__energy_level -= energy_cost
            self.__mission_count += 1
            print(f"✅ Mission completed! Missions: {self.__mission_count}, Energy: {self.__energy_level}%")
            return True
        print("❌ Too tired for this mission!")
        return False
    
    def rest(self):
        self.__energy_level = min(100, self.__energy_level + 30)
        print(f"😴 {self.name} rests. Energy: {self.__energy_level}%")
    
    # Private method (encapsulation)
    def __check_energy(self, required_energy):
        return self.__energy_level >= required_energy
    
    # Protected method (accessible to subclasses)
    def _reveal_secret(self):
        return f"My secret identity is {self._secret_identity}"
    
    # Public getter method (encapsulation)
    def get_energy_level(self):
        return self.__energy_level
    
    def get_mission_count(self):
        return self.__mission_count
    
    # Polymorphic method (to be overridden by subclasses)
    def special_ability(self):
        return f"{self.name} has no special ability yet."
    
    def __str__(self):
        return f"Superhero: {self.name} | Powers: {', '.join(self.powers)} | Energy: {self.__energy_level}%"

# Inherited class 1
class FlyingHero(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, flight_speed, energy_level=100):
        super().__init__(name, secret_identity, powers, weakness, energy_level)
        self.flight_speed = flight_speed  # km/h
        self.__altitude = 0
    
    # Override parent method (polymorphism)
    def use_power(self, power_name):
        if power_name == "fly" and self._Superhero__check_energy(20):
            self._Superhero__energy_level -= 20
            self.__altitude = 1000
            print(f"✈️ {self.name} takes flight at {self.flight_speed} km/h! Altitude: {self.__altitude}m")
            return True
        return super().use_power(power_name)
    
    # New method specific to FlyingHero
    def land(self):
        if self.__altitude > 0:
            self.__altitude = 0
            print(f"🛬 {self.name} lands safely.")
        else:
            print(f"{self.name} is already on the ground.")
    
    # Override special_ability method
    def special_ability(self):
        return f"{self.name} can fly at supersonic speeds up to {self.flight_speed} km/h!"

# Inherited class 2
class TechHero(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, gadgets, energy_level=100):
        super().__init__(name, secret_identity, powers, weakness, energy_level)
        self.gadgets = gadgets
        self.__invention_count = 0
    
    # Override parent method
    def complete_mission(self, mission_difficulty):
        # Tech heroes use 25% less energy for tech-related missions
        energy_cost = max(5, mission_difficulty * 15 - 5)
        if self._Superhero__check_energy(energy_cost):
            self._Superhero__energy_level -= energy_cost
            self._Superhero__mission_count += 1
            self.__invention_count += 1
            print(f"🔧 Tech mission completed! New gadget invented! Total: {self.__invention_count}")
            return True
        return super().complete_mission(mission_difficulty)
    
    # New method specific to TechHero
    def use_gadget(self, gadget_name):
        if gadget_name in self.gadgets:
            print(f"🛠️ {self.name} uses {gadget_name}!")
            return True
        print(f"{gadget_name} not available in {self.name}'s arsenal!")
        return False
    
    # Override special_ability method
    def special_ability(self):
        return f"{self.name} can create amazing gadgets like: {', '.join(self.gadgets)}"

# Demonstration
if __name__ == "__main__":
    print("🦸 SUPERHERO SIMULATION 🦸")
    print("=" * 50)
    
    # Create superheroes
    superman = FlyingHero(
        "Superman", "Clark Kent",
        ["fly", "super strength", "heat vision", "x-ray vision"],
        "Kryptonite", 2000
    )
    
    iron_man = TechHero(
        "Iron Man", "Tony Stark",
        ["repulsor beams", "flight", "AI assistance"],
        "Power source depletion",
        ["Arc Reactor", "J.A.R.V.I.S.", "Nanotech Suit", "Missiles"]
    )
    
    # Demonstrate functionality
    print(superman)
    print(iron_man)
    print()
    
    # Use powers and methods
    superman.use_power("fly")
    superman.use_power("super strength")
    superman.complete_mission(3)
    print(superman._reveal_secret())  # Protected method
    print()
    
    iron_man.use_gadget("Nanotech Suit")
    iron_man.complete_mission(2)
    iron_man.use_power("repulsor beams")
    print()
    
    # Demonstrate polymorphism
    heroes = [superman, iron_man]
    for hero in heroes:
        print(hero.special_ability())
    
    print()
    
    # Demonstrate encapsulation - trying to access private attributes directly
    try:
        print(superman.__energy_level)  # This will fail
    except AttributeError:
        print("❌ Cannot access private attribute __energy_level directly!")
    
    # Access through getter method
    print(f"Superman's energy: {superman.get_energy_level()}%")
    print(f"Iron Man's missions: {iron_man.get_mission_count()}")
    
    # Rest and recover energy
    superman.rest()
    iron_man.rest()