import os
import csv

election_data_2_csv = os.path.join("Resources", "election_data.csv")
output_file = "election_results.txt"

with open(election_data_2_csv) as my_file, open(output_file, "w") as output:
    csv_reader = csv.reader(my_file, delimiter=",")

    # 1. ALL VOTES
    next(csv_reader, None)

    all_votes = []

    for row in csv_reader:
        vote_id = row[0]
        all_votes.append(vote_id)

    total_votes = len(all_votes)
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------", file=output)
    print(f"Total Votes: {total_votes}", file=output)
    print("-------------------------", file=output)

    # 2.0 CANTIDAD DE CANDIDATOS QUE TIENEN VOTOS
    my_file.seek(0)
    next(csv_reader, None)
    unique_candidate = set()

    for row in csv_reader:
        candidate = row[2]
        unique_candidate.add(candidate)

    total_candidate = len(unique_candidate)
    print(f"Amount of candidates: {total_candidate}")
    print("-------------------------", file=output)
    print(f"Amount of candidates: {total_candidate}", file=output)
    print("-------------------------", file=output)

    # 2.1 A complete list of candidates who received votes
    my_file.seek(0)
    next(csv_reader, None)
    unique_candidate_2 = set()

    for row in csv_reader:
        candidate = row[2]
        unique_candidate.add(candidate)

    for candidate in unique_candidate:
        print(candidate)

    print("-------------------------", file=output)
    for candidate in unique_candidate:
        print(candidate, file=output)

    print("-------------------------", file=output)

    # 3. The total number of votes each candidate won
    my_file.seek(0)
    next(csv_reader, None)
    votes_count = 0
    candidate_votes = {}

    for row in csv_reader:
        candidate = row[2]

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        percentage_rounded = round(percentage, 3)
        print(f"{candidate}: {percentage_rounded}% ({votes})")
        print(f"{candidate}: {percentage_rounded}% ({votes})", file=output)

    print("-------------------------", file=output)

    # 4. Winner
    winner = max(candidate_votes, key=candidate_votes.get)
    print(f"Winner: {winner}")
    print(f"Winner: {winner}", file=output)

print("Los resultados se han guardado en el archivo 'election_results.txt'.")
