chai_type="Ginger Tea"
customer_name="Prashant Maurya"

print(f"Order for {chai_type} by {customer_name}")

chai_description = "Aromatic and Bold"
print(f"First Word:{chai_description[0:8]}")
print(f"Last Word:{chai_description[:8]}")
print(f"Last Word:{chai_description[12:]}")
print(f"Reverse Word:{chai_description[::-1]}")

label_text = "Special Chai"
encoded_text = label_text.encode("utf-8")
print(f"Non-Encoded_Text:{label_text}")
print(f"Encoded_Text:{encoded_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"Decoded Text: {decoded_text}")