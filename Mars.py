import random
import time
import telebot

# Replace 'YOUR_TELEGRAM_TOKEN' with your actual Telegram bot token
bot = telebot.TeleBot('6177428008:AAEewf2ZGq657fvMqJ6oqH4tYoYvpaP68p8')

events = [
    "The astronaut encounters an alien species on Mars!",
    "The spaceship sustains minor damage but remains functional.",
    "The astronaut discovers a new planet during the journey.",
    "The astronaut loses direction and struggles to navigate.",
    "A meteor shower poses a threat to the spaceship.",
    "A technical malfunction requires immediate repairs.",
    "The astronaut finds an ancient Martian artifact.",
    "A communication glitch temporarily disconnects the astronaut from Earth.",
    "The spaceship's oxygen levels drop unexpectedly.",
    "The astronaut witnesses a spectacular Martian sunrise.",
    "A sudden solar flare disrupts communication with Earth.",
    "The spaceship's food supply is contaminated and becomes inedible.",
    "The astronaut stumbles upon a hidden Martian cave system.",
    "The spaceship's power source starts malfunctioning.",
    "The astronaut encounters a hostile extraterrestrial creature.",
    "The spaceship's navigation system fails, leaving the astronaut stranded.",
    "The astronaut discovers a previously unknown Martian plant species.",
    "A mysterious signal from deep space grabs the astronaut's attention.",
    "The spaceship's communication device picks up an unintelligible transmission.",
    "The astronaut faces a dangerous Martian sandstorm.",
    "The spaceship's engines malfunction, causing a delay in the journey.",
    "The astronaut experiences a minor injury but recovers quickly.",
    "A swarm of cosmic particles disrupts the spaceship's electronic systems.",
    "The astronaut encounters an abandoned Martian outpost.",
    "The spaceship's AI system develops a glitch and starts acting strangely.",
    "The astronaut captures breathtaking photographs of the Martian landscape.",
    "A critical supply onboard the spaceship runs out unexpectedly.",
    "The astronaut receives a message from an unknown source.",
    "The spaceship's shield protects it from a powerful solar flare.",
    "The astronaut discovers evidence of past life on Mars.",
    "A mysterious illness affects the astronaut, requiring medical attention.",
    "The spaceship's fuel levels drop dangerously low.",
    "The astronaut discovers a frozen lake beneath the Martian surface.",
    "The spaceship's communication antenna gets damaged, hindering contact.",
    "The astronaut witnesses a rare Martian dust devil in action.",
    "The spaceship passes through a dense asteroid belt.",
    "The astronaut becomes disoriented due to a magnetic anomaly.",
    "The spaceship's robotic assistant malfunctions and requires repair.",
    "The astronaut stumbles upon a field of Martian geysers.",
    "A navigation error leads the astronaut off-course.",
    "The spaceship's solar panels get covered in a thick layer of Martian dust.",
    "The astronaut experiences a moment of homesickness.",
    "A malfunction in the life support system causes a brief scare.",
    "The spaceship's communication with Earth is intercepted by an unknown entity.",
    "The astronaut discovers a natural cave system that leads to an underground Martian lake.",
    "The spaceship's heat shields protect it from a dangerous solar storm.",
    "The astronaut witnesses a rare Martian meteor shower.",
    "A small fire breaks out on the spaceship but is quickly extinguished.",
    "The spaceship's AI develops a glitch and starts speaking in riddles.",
    "The astronaut discovers a field of Martian crystals with unknown properties.",
    "The spaceship's autopilot system fails, requiring manual control.",
    "The astronaut encounters a lost Martian rover from a previous mission.",
    "The spaceship's navigation system leads the astronaut to an unexpected detour.",
    "The astronaut experiences a moment of weightlessness in space.",
    "The spaceship's main engine suffers a temporary power loss.",
    "The astronaut encounters a swarm of bioluminescent Martian insects.",
    "The spaceship's airlock malfunctions, posing a temporary safety risk.",
    "The astronaut's spacesuit sustains a minor tear but remains functional.",
    "The spaceship picks up a mysterious radio signal from an unknown origin.",
    "The astronaut discovers an ancient Martian temple buried beneath the surface.",
    "The spaceship narrowly avoids colliding with a large asteroid.",
    "The astronaut's telescope captures a stunning view of Mars' moons.",
    "The spaceship's supply of drinking water gets contaminated.",
    "The astronaut witnesses a Martian sandstorm with unusually vibrant colors.",
    "A power surge causes temporary disruptions in the spaceship's systems.",
    "The astronaut stumbles upon a field of Martian fossils.",
    "The spaceship's radar detects a large underground cavity on Mars.",
    "The astronaut experiences a moment of solitude and reflection in space.",
    "The spaceship's emergency beacon accidentally activates, causing confusion.",
    "The astronaut discovers a hidden cache of supplies left by a previous mission.",
    "The spaceship's solar panels malfunction, requiring repairs.",
    "The astronaut encounters a group of friendly alien creatures on Mars.",
    "The spaceship's communication with Earth is briefly interrupted by a solar flare.",
    "The astronaut witnesses a stunning alignment of Mars and Earth in the night sky.",
    "The spaceship's robotic arm malfunctions, hindering repairs.",
    "The astronaut stumbles upon an ancient Martian city in ruins.",
    "A malfunctioning thruster causes the spaceship to spin uncontrollably.",
    "The astronaut captures a mesmerizing video of the Martian auroras.",
    "The spaceship's main computer encounters a critical software error.",
    "The astronaut discovers a vast underground Martian cavern.",
    "The spaceship's air filtration system malfunctions, requiring immediate attention.",
    "The astronaut encounters a swarm of Martian fireflies lighting up the night.",
    "The spaceship's communication with Earth is temporarily jammed by unknown interference.",
    "The astronaut witnesses a solar eclipse from the surface of Mars.",
    "The spaceship's navigation system gets locked in a loop, repeating coordinates.",
    "The astronaut discovers a field of Martian flowers with bioluminescent petals.",
    "The spaceship's food synthesizer malfunctions, limiting meal options.",
    "The astronaut experiences a moment of awe while observing the Martian landscape.",
    "A sudden change in atmospheric pressure causes turbulence inside the spaceship.",
    "The astronaut stumbles upon a hidden Martian underground oasis.",
    "The spaceship's propulsion system encounters a minor hiccup but recovers.",
    "The astronaut captures a breathtaking panoramic image of the Martian desert.",
    "The spaceship's radio picks up mysterious whispers in an unknown language.",
    "The astronaut witnesses a spectacular meteorite impact on Mars.",
    "A solar wind gust temporarily disrupts the spaceship's power supply.",
    "The astronaut discovers an abandoned Martian spaceship from a bygone era.",
    "The spaceship's artificial gravity malfunctions, causing brief weightlessness.",
    "The astronaut encounters a large Martian creature with bioluminescent markings.",
    "The spaceship's communication with Earth is temporarily lost due to a solar blackout.",
    "The astronaut observes a rare alignment of Mars' moons from the spaceship.",
    "The spaceship's radar detects an underground network of tunnels on Mars.",
    "The astronaut experiences a moment of deep introspection while gazing at Earth.",
    "The spaceship's engine emits an unusual sound, but functionality remains unaffected.",
    "The astronaut stumbles upon a field of Martian rock formations resembling sculptures.",
    "A navigation glitch causes the spaceship to briefly veer off course.",
    "The spaceship's solar panels receive a power boost from a passing comet's tail.",
    "The astronaut's personal diary goes missing but is later found hidden in a storage compartment.",
]


def simulate_journey():
    day = 1
    while True:
        # Generate a random event
        event = random.choice(events)

        # Prepare the journal entry for the event
        journal_entry = f"Space Exploration Journal Day {day}: "
        journal_entry += f" {event.lower()}"

        # Print the journal entry
        print(journal_entry)

        # Send the journal entry via Telegram bot
        bot.send_message('1285682450', journal_entry)

        # Increment the day count
        day += 1

        # Delay for 6 hours (in seconds)
        time.sleep(6 * 60 * 60)

simulate_journey()
