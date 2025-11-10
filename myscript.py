import os
import sys

# Définir les commits good et bad
bad_commit = "c1a4be04b972b6c17db242fc37752ad517c29402"  # Commit le plus récent (bad)
good_commit = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"  # Commit connu comme bon

# Démarrer git bisect
print(f"Starting git bisect between {good_commit} (good) and {bad_commit} (bad)")
os.system(f"git bisect start {bad_commit} {good_commit}")

# Exécuter git bisect automatiquement avec les tests
print("Running git bisect with automated testing...")
result = os.system("git bisect run python manage.py test")

# Afficher le résultat
if result == 0:
    print("\nGit bisect completed successfully!")
else:
    print("\nGit bisect encountered an error")
    sys.exit(1)

# Reset git bisect pour revenir à l'état normal
os.system("git bisect reset")