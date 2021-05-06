// SPDX-License-Identifier: Apache-2.0

/*
  Sample Chaincode based on Demonstrated Scenario

 This code is based on code written by the Hyperledger Fabric community.
  Original code can be found here: https://github.com/hyperledger/fabric-samples/blob/release/chaincode/fabcar/fabcar.go
 */

package main

/* Imports
* 4 utility libraries for handling bytes, reading and writing JSON,
formatting, and string manipulation
* 2 specific Hyperledger Fabric specific libraries for Smart Contracts
*/
import (
	"bytes"
	"encoding/json" 
	"fmt"
	"strconv"

	"github.com/hyperledger/fabric/core/chaincode/shim"
	sc "github.com/hyperledger/fabric/protos/peer"
)

// Define the Smart Contract structure
type SmartContract struct {
}

/* Define Drug structure, with 4 properties.
Structure tags are used by encoding/json library
*/
type Drug struct {
	Manufacturer string `json:"manufacturer"`
	Timestamp string `json:"timestamp"`
	Location  string `json:"location"`
	Holder  string `json:"holder"`
}

/*
 * The Init method *
 called when the Smart Contract "drug-chaincode" is instantiated by the network
 * Best practice is to have any Ledger initialization in separate function
 -- see initLedger()
 */
func (s *SmartContract) Init(APIstub shim.ChaincodeStubInterface) sc.Response {
	return shim.Success(nil)
}

/*
 * The Invoke method *
 called when an application requests to run the Smart Contract "drug-chaincode"
 The app also specifies the specific smart contract function to call with args
 */
func (s *SmartContract) Invoke(APIstub shim.ChaincodeStubInterface) sc.Response {

	// Retrieve the requested Smart Contract function and arguments
	function, args := APIstub.GetFunctionAndParameters()
	// Route to the appropriate handler function to interact with the ledger
	if function == "queryDrug" {
		return s.queryDrug(APIstub, args)
	} else if function == "initLedger" {
		return s.initLedger(APIstub)
	} else if function == "recordDrug" {
		return s.recordDrug(APIstub, args)
	} else if function == "queryAllDrug" {
		return s.queryAllDrug(APIstub)
	} else if function == "changeDrugHolder" {
		return s.changeDrugHolder(APIstub, args)
	}

	return shim.Error("Invalid Smart Contract function name.")
}

/*
 * The queryDrug method *
Used to view the records of one particular drug
It takes one argument -- the key for the drug in question
 */
func (s *SmartContract) queryDrug(APIstub shim.ChaincodeStubInterface, args []string) sc.Response {

	if len(args) != 1 {
		return shim.Error("Incorrect number of arguments. Expecting 1")
	}

	drugAsBytes, _ := APIstub.GetState(args[0])
	if drugAsBytes == nil {
		return shim.Error("Could not locate drug")
	}
	return shim.Success(drugAsBytes)
}

/*
 * The initLedger method *
Will add test data (10 drug catches)to our network
 */
func (s *SmartContract) initLedger(APIstub shim.ChaincodeStubInterface) sc.Response {
	drug := []Drug{
		Drug{Manufacturer: "insulin", Location: "67.0006, -70.5476", Timestamp: "1504054225", Holder: "Fortis Hospital"},
		Drug{Manufacturer: "insulin", Location: "91.2395, -49.4594", Timestamp: "1504057825", Holder: "Lifeline Hospital"},
		Drug{Manufacturer: "insulin", Location: "20, 40", Timestamp: "7894117101", Holder: "Sai Pharma"},
		Drug{Manufacturer: "insulin", Location: "58.0148, 59.01391", Timestamp: "1493517025", Holder: "Suvidha Clinic"},
		Drug{Manufacturer: "insulin", Location: "-45.0945, 0.7949", Timestamp: "1496105425", Holder: "Breach candy Hospital"},
		Drug{Manufacturer: "insulin", Location: "20, 40", Timestamp: "4564567801", Holder: "Sai Pharma"},
		Drug{Manufacturer: "insulin", Location: "-155.2304, -15.8723", Timestamp: "1494117101", Holder: "Hinduja Hospital"},
			}

	i := 0
	for i < len(drug) {
		fmt.Println("i is ", i)
		drugAsBytes, _ := json.Marshal(drug[i])
		APIstub.PutState(strconv.Itoa(i+1), drugAsBytes)
		fmt.Println("Added", drug[i])
		i = i + 1
	}

	return shim.Success(nil)
}

/*
 * The recordDrug method *
This method takes in five arguments (attributes to be saved in the ledger).
 */
func (s *SmartContract) recordDrug(APIstub shim.ChaincodeStubInterface, args []string) sc.Response {

	if len(args) != 5 {
		return shim.Error("Incorrect number of arguments. Expecting 5")
	}
	//mycode
	d, _ := APIstub.GetState(args[0])
	if d == nil {
	
//mycode
	var drug = Drug{ Manufacturer: args[1], Location: args[2], Timestamp: args[3], Holder: args[4] }

	drugAsBytes, _ := json.Marshal(drug)
	err := APIstub.PutState(args[0], drugAsBytes)
	if err != nil {
		return shim.Error(fmt.Sprintf("Failed to record drug packet: %s", args[0]))
	}

	return shim.Success(nil)
	} else {

	drugAsBytes, _ := APIstub.GetState(args[0])
	drug := Drug{}

	json.Unmarshal(drugAsBytes, &drug)
	// Normally check that the specified argument is a valid holder of drug
	// we are skipping this check for this example
	drug.Holder = args[4] + " (Suspicious) "

	drugAsBytes, _ = json.Marshal(drug)
	err := APIstub.PutState(args[0], drugAsBytes)
	if err != nil {
		return shim.Error(fmt.Sprintf("Failed to change drug holder: %s", args[0]))
	}

	return shim.Success(nil)
}

}

/*
 * The queryAllDrug method *
allows for assessing all the records added to the ledger(all drug catches)
This method does not take any arguments. Returns JSON string containing results.
 */
func (s *SmartContract) queryAllDrug(APIstub shim.ChaincodeStubInterface) sc.Response {

	startKey := "0"
	endKey := "999"

	resultsIterator, err := APIstub.GetStateByRange(startKey, endKey)
	if err != nil {
		return shim.Error(err.Error())
	}
	defer resultsIterator.Close()

	// buffer is a JSON array containing QueryResults
	var buffer bytes.Buffer
	buffer.WriteString("[")

	bArrayMemberAlreadyWritten := false
	for resultsIterator.HasNext() {
		queryResponse, err := resultsIterator.Next()
		if err != nil {
			return shim.Error(err.Error())
		}
		// Add comma before array members,suppress it for the first array member
		if bArrayMemberAlreadyWritten == true {
			buffer.WriteString(",")
		}
		buffer.WriteString("{\"Key\":")
		buffer.WriteString("\"")
		buffer.WriteString(queryResponse.Key)
		buffer.WriteString("\"")

		buffer.WriteString(", \"Record\":")
		// Record is a JSON object, so we write as-is
		buffer.WriteString(string(queryResponse.Value))
		buffer.WriteString("}")
		bArrayMemberAlreadyWritten = true
	}
	buffer.WriteString("]")

	fmt.Printf("- queryAllDrug:\n%s\n", buffer.String())

	return shim.Success(buffer.Bytes())
}

/*
 * The changeDrugHolder method *
The data in the world state can be updated with who has possession.
This function takes in 2 arguments, drug id and new holder name.
 */
func (s *SmartContract) changeDrugHolder(APIstub shim.ChaincodeStubInterface, args []string) sc.Response {

	if len(args) != 4 {
		return shim.Error("Incorrect number of arguments. Expecting 2")
	}

	drugAsBytes, _ := APIstub.GetState(args[0])
	if drugAsBytes == nil {
		return shim.Error("Could not locate drug")
	}

	drug := Drug{}

	json.Unmarshal(drugAsBytes, &drug)
	// Normally check that the specified argument is a valid holder of drug
	// we are skipping this check for this example
	drug.Holder = args[1]
	drug.Location = args[2]
	drug.Timestamp =  args[3]

	drugAsBytes, _ = json.Marshal(drug)
	err := APIstub.PutState(args[0], drugAsBytes)
	if err != nil {
		return shim.Error(fmt.Sprintf("Failed to change drug holder: %s", args[0]))
	}

	return shim.Success(nil)
}

/*
 * main function *
calls the Start function
The main function starts the chaincode in the container during instantiation.
 */
func main() {

	// Create a new Smart Contract
	err := shim.Start(new(SmartContract))
	if err != nil {
		fmt.Printf("Error creating new Smart Contract: %s", err)
	}
}
