from tools import query_relevant_policies

# Test query for a non-compliant liability clause
test_clause = "The vendor limits its total liability for any data breaches to $100,000 USD."

results = query_relevant_policies(test_clause)

print("🔍 Policy Match Results:\n")
for policy in results:
    print(f"📌 Policy ID: {policy['policy_id']} | Category: {policy['category']}")
    print(f"   Content: {policy['content']}\n")