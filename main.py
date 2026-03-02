import numpy as np
import time
import pandas as pd
from ace_lib import SingleSession, generate_alpha, simulate_alpha_list_multi
from helpful_functions import prettify_result

# Search space constants
GROUPS = ['country', 'industry', 'subindustry', 'sector']
DAYS_RANGE = range(20, 1001, 50)
DECAY_RANGE = range(10, 111, 10)
NEUTRALIZATIONS = ['industry', 'subindustry', 'sector', 'crowding', 'market', 'statistical']

def run_alpha_search():
    session = SingleSession() # Singleton session management from ace_lib
    alpha_configs = []

    print(f"Starting Grid Search. Total combinations to test: {len(GROUPS) * len(DAYS_RANGE) * len(DECAY_RANGE) * len(NEUTRALIZATIONS)}")

    # Generate alpha configurations for testing
    for group in GROUPS:
        for days in DAYS_RANGE:
            for decay in DECAY_RANGE:
                for neutr in NEUTRALIZATIONS:
                    # Template formula with hierarchical normalization (Z-score -> Rank -> Time Rank)
                    expression = f"ts_rank(group_rank(group_zscore(((high+low)/2-close)/close, {group}), {group}), {days})"
                    
                    config = {
                        'expression': expression,
                        'region': 'EUR',
                        'universe': 'TOPCS1600',
                        'neutralization': neutr.upper(),
                        'decay': decay,
                        'delay': 1,
                        'group_param': group,
                        'days_param': days,
                        'decay_param': decay,
                        'neutr_param': neutr,
                        'name': f"Alpha_{group}_d{days}_dec{decay}_{neutr}"
                    }
                    alpha_configs.append(config)

    # Execute batch simulation using ThreadPool parallelism from ace_lib
    results = simulate_alpha_list_multi(alpha_configs)
    
    # Save all results to CSV for further analysis
    if results:
        df = pd.DataFrame(results)
        filename = f"grid_search_results_{int(time.time())}.csv"
        df.sort_values(by='sharpe', ascending=False, inplace=True)
        df.to_csv(filename, index=False)
        print(f"Full results saved to: {filename}")
    
    return results

def find_best_alpha(results):
    # Filter results based on defined quantitative thresholds
    valid_alphas = [
        res for res in results 
        if res.get('sharpe', 0) >= 1.58 and res.get('fitness', 0) >= 1.0
    ]
    
    # Sort candidates by Sharpe Ratio in descending order
    valid_alphas.sort(key=lambda x: x.get('sharpe', 0), reverse=True)
    
    if valid_alphas:
        best = valid_alphas[0]
        print("\n" + "="*50)
        print("🏆 BEST ALPHA FOUND:")
        print(f"Expression: {best['expression']}")
        print(f"Sharpe: {best['sharpe']} | Fitness: {best['fitness']}")
        print(f"Turnover: {best['turnover']}%")
        print("="*50)
        return best
    else:
        print("No alphas met the criteria.")
        return None

if __name__ == "__main__":
    start_time = time.time()
    all_results = run_alpha_search()
    best_one = find_best_alpha(all_results)
    
    print(f"\nSearch finished in {round((time.time() - start_time)/60, 2)} minutes.")