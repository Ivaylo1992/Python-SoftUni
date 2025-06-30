from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    ORACLE = {
        1: 1_500_000,
        2: 800_000,
    }

    HONDA = {
        1: 20_000,
        2: 20_000,
        3: 20_000,
        4: 20_000,
        5: 20_000,
        6: 20_000,
        7: 20_000,
        8: 20_000,
        9: 10_000,
        10: 10_000
    }

    def calculate_revenue_after_race(self, race_pos: int):
        oracle_bonus = self.ORACLE.get(race_pos) if self.ORACLE.get(race_pos) else 0
        honda_bonus = self.HONDA.get(race_pos) if self.HONDA.get(race_pos) else 0

        revenue = oracle_bonus + honda_bonus - 250_000

        self.budget += revenue

        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"