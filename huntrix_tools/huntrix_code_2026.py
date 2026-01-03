import random
import time


def huntrix_fan(name, aura=100, blessings=0, combo=1):
    """
    Simulates a Huntrix fan aura system.
    - name: fan's name
    - aura: starting aura points
    - blessings: number of rituals/blessings performed
    - combo: multiplier for streak rituals
    """
    # Ritual blessing
    blessings += 1
    aura_gain = random.randint(10, 25) * combo
    aura += aura_gain

    # Badge unlocks
    badges = []
    if blessings % 5 == 0:
        badges.append("🔥 Ritual Streak")
    if aura >= 500:
        badges.append("🌟 Legendary Fan")

    # Timestamp for lore flavor
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    return {
        "fan": name,
        "aura": aura,
        "blessings": blessings,
        "combo": combo,
        "aura_gain": aura_gain,
        "badges": badges,
        "last_ritual": timestamp,
    }


# Example usage
fan_status = huntrix_fan("Abinav", aura=120, blessings=4, combo=2)
print(fan_status)
