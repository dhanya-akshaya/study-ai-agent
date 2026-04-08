import PyPDF2
import re
import os

class StudyAI:
    def __init__(self):
        self.notes_text = ""
        self.data = []

    def clean_text(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def load_file(self, path):
        if not os.path.exists(path):
            print("❌ File not found.")
            return False

        try:
            text = ""

            if path.endswith(".pdf"):
                with open(path, "rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        t = page.extract_text()
                        if t:
                            text += t + " "

            elif path.endswith(".txt"):
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()

            else:
                print("❌ Unsupported format.")
                return False

            self.notes_text = self.clean_text(text)
            self.process_notes()

            print(f"✅ File loaded successfully! ({len(self.data)} topics)")
            return True

        except Exception as e:
            print("❌ Error:", e)
            return False

    def process_notes(self):
        sentences = re.split(r'(?<=[.!?])\s+', self.notes_text)

        self.data = []
        current_topic = None

        for s in sentences:
            s = s.strip()

            if len(s) < 15:
                continue

            if " is " in s:
                topic = s.split(" is ")[0].strip()

                if topic.lower() not in ["it", "this", "that", "example"]:
                    current_topic = {
                        "topic": topic,
                        "content": s
                    }
                    self.data.append(current_topic)

            elif current_topic:
                first_word = s.split()[0].lower()

                if first_word in ["it", "this", "they"]:
                    current_topic["content"] += " " + s

        unique = {}
        for item in self.data:
            base = re.sub(r'\(.*?\)', '', item["topic"]).strip().lower()

            if base not in unique or len(item["content"]) > len(unique[base]["content"]):
                unique[base] = item

        self.data = list(unique.values())

    def find_best_answer(self, query):
        query = query.lower()

        # exact match
        for item in self.data:
            topic = item["topic"].lower()
            if topic in query:
                return item["content"]

        # keyword match
        best = None
        score = 0

        query_words = set(query.split())

        for item in self.data:
            topic_words = set(item["topic"].lower().split())
            match = len(query_words & topic_words)

            if match > score:
                score = match
                best = item["content"]

        # fallback
        if not best:
            for item in self.data:
                if any(word in item["content"].lower() for word in query_words):
                    return item["content"]

        return best

    def summary(self):
        print("\n--- 📝 SUMMARY ---\n")

        for item in self.data:
            print("•", item["content"])

    def questions(self):
        print("\n--- ❓ IMPORTANT QUESTIONS ---\n")

        seen = set()
        qno = 1

        for item in self.data:
            topic = item["topic"]

            if ":" in topic:
                topic = topic.split(":")[0]

            topic = topic.strip()

            base = re.sub(r'\(.*?\)', '', topic).strip().lower()

            if base in seen:
                continue

            seen.add(base)

            print(f"Q{qno}: What is {topic}?")
            qno += 1

    def flashcards(self):
        print("\n--- 🧠 FLASHCARDS ---\n")

        seen = set()
        qno = 1

        for item in self.data:
            topic = item["topic"]

            if ":" in topic:
                topic = topic.split(":")[0]

            topic = topic.strip()

            base = re.sub(r'\(.*?\)', '', topic).strip().lower()

            if base in seen:
                continue

            seen.add(base)

            print(f"Q{qno}: What is {topic}?")
            print(f"A{qno}: {item['content']}\n")

            qno += 1

    def search(self, keyword):
        print("\n🔍 Results:\n")

        found = False

        for item in self.data:
            if keyword.lower() in item["content"].lower():
                print("-", item["content"])
                found = True

        if not found:
            print("No results found.")

    def chat(self):
        print("\n🤖 Chat Mode (type exit)\n")

        while True:
            q = input("You: ")

            if q.lower() == "exit":
                break

            ans = self.find_best_answer(q)

            if ans:
                print("AI:", ans)
            else:
                print("AI: Try asking differently.")

def main():
    ai = StudyAI()

    print("🤖 Study AI Agent")

    path = input("Enter file path: ").strip('"')

    if not ai.load_file(path):
        return

    while True:
        print("\n" + "="*35)
        print("1. Ask Question")
        print("2. Summary")
        print("3. Questions")
        print("4. Flashcards")
        print("5. Search")
        print("6. Chat")
        print("7. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            q = input("Ask: ")
            ans = ai.find_best_answer(q)
            print("\n🧠", ans if ans else "No answer found.")

        elif ch == "2":
            ai.summary()

        elif ch == "3":
            ai.questions()

        elif ch == "4":
            ai.flashcards()

        elif ch == "5":
            k = input("Keyword: ")
            ai.search(k)

        elif ch == "6":
            ai.chat()

        elif ch == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
