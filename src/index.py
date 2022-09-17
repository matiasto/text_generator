from services import ReadService, CleanService, MarkovModel, GenerateService


def main():
    read_service = ReadService()
    while True:
        available_stories = read_service.available_stories
        print("\nAvailable stories:")
        for i, story in enumerate(available_stories):
            print(f"{i + 1}. {story}")
        print("0. Exit\n")
        choice = input("Choose a story: ")
        if choice == "0":
            break
        try:
            choice = int(choice)
            if choice < 0 or choice > len(available_stories):
                raise ValueError
        except ValueError:
            print("Invalid choice")
            continue
        story = available_stories[choice - 1]
        read_service.text = story
        clean_service = CleanService(read_service.text)
        markov_model = MarkovModel(clean_service.clean_text)
        starting_word = markov_model.get_random_starting_word()
        generate = GenerateService(starting_word, markov_model.model)
        print("\nGenerated text:")
        print(generate.generated_text)
        print("\n")


if __name__ == "__main__":
    main()
