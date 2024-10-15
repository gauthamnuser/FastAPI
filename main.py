from fastapi import FastAPI

app = FastAPI()

@app.get("/simple_interest/{total_amount}/{years}/{percent}")
def simple_interest(total_amount,years,percent):
    principle=int(total_amount)
    rate=int(percent)/100
    time=int(years)
    interest=principle*rate*time
    return {"total_amount": total_amount,"interest": interest}

@app.get("/compound_interest/{total_amount}/{years}/{percent}")
def compound_interest(total_amount,years,percent):
    principle=int(total_amount)
    rate=int(percent)/100
    time=int(years)
    rate2=(1+rate)**time
    interest=(principle*rate2)-principle
    return {"total_amount": total_amount,"interest": interest}

