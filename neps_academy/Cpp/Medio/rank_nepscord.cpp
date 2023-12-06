#include <bits/stdc++.h>

struct Player {
    std::string username;
    int xp;
    int last_minute;
};

int main() {
    std::vector<Player> rank;
    std::vector<std::string> usernames;

    int n, k;
    std::cin >> n >> k;

    for (int i = 0; i < n; ++i) {
        std::string u;
        int m;
        std::cin >> u >> m;

        if (std::find(usernames.begin(), usernames.end(), u) == usernames.end()) {
            usernames.push_back(u);
            rank.push_back({u, 25, m});
        } else {
            for (auto& r : rank) {
                if (r.username == u) {
                    if (m >= r.last_minute + k) {
                        r.xp += 25;
                    }
                    r.last_minute = m;
                    break;
                }
            }
        }
    }

    for (auto& ra : rank) {
        ra.xp = 0;
    }

    int max_xp = std::max_element(rank.begin(), rank.end(), [](const Player& a, const Player& b) {
        return a.xp < b.xp;
    })->xp;

    std::sort(rank.begin(), rank.end(), [](const Player& a, const Player& b) {
        return a.username < b.username;
    });

    std::vector<Player> final_rank;
    for (const auto& ra : rank) {
        if (ra.xp == max_xp) {
            final_rank.push_back(ra);
        }
        if (final_rank.size() == 3) {
            break;
        }
    }

    if (final_rank.size() < 3) {
        for (const auto& ra : rank) {
            if (ra.xp < max_xp) {
                final_rank.push_back(ra);
            }
            if (final_rank.size() == 3) {
                break;
            }
        }
    }

    std::cout << "--Rank do Nepscord--" << std::endl;
    for (int i = 0; i < 3; ++i) {
        if (i < final_rank.size()) {
            std::cout << '#' << i + 1 << ". " << final_rank[i].username << " - "
                      << (final_rank[i].xp >= 100 ? "Nivel 2" : "Nivel 1") << std::endl;
        } else {
            std::cout << '#' << i + 1 << std::endl;
        }
    }

    return 0;
}
