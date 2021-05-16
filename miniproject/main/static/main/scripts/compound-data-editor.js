
class CompoundDataEditor extends HTMLElement{
    constructor(){
        super();
        this.createEditor();
    }

    createEditor(){
        this.tableWrapper = document.createElement("div");
        this.table = document.createElement("table");

        this.tableWrapper.classList.add("table-wrapper");
        
        this.tableWrapper.append(this.table);
        this.append(this.tableWrapper);

        let addRowBtn = document.createElement("div");
        addRowBtn.classList.add("add-row-btn");
        addRowBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>ic_add_24px</title>
            <g>
                <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path>
            </g>
        </svg>
        New row
        ` ;
        addRowBtn.addEventListener("click",()=>this.addRow());

        let addFieldBtn = document.createElement("div");
        addFieldBtn.classList.add("add-field-btn");
        addFieldBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>ic_add_24px</title>
            <g>
                <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path>
            </g>
        </svg>
        ` ;
        addFieldBtn.addEventListener("click",()=>this.addField());

        // add basic template
        this.header = this.table.createTHead() ;
        let headerRow = this.header.insertRow();
        headerRow.insertCell(-1).innerHTML = "#";
        headerRow.insertCell(-1).innerHTML = "Label";
        headerRow.insertCell(-1).append(addFieldBtn);

        this.footer = this.table.createTFoot() ;
        let footerRow = this.footer.insertRow();
        footerRow.insertCell(-1);
        footerRow.insertCell(-1).append(addRowBtn);
        footerRow.insertCell(-1);

        this.header = this.table.createTBody() ;
    }

    addRow(){
        let newRow = this.table.tBodies[0].insertRow(-1);
        let headerCells = [...this.table.tHead.rows[0].cells] ;
        headerCells.forEach((cell,i)=>{
            let newCell = newRow.insertCell(-1);
            if(i==1){
                newCell.innerHTML = `
                    <div data-name="label" contenteditable></div>
                `;
            } else if(i>1 && i != headerCells.length - 1) {
                let valueDiv = document.createElement("div");
                valueDiv.setAttribute("data-name","value");
                valueDiv.contentEditable = true ;
                valueDiv.addEventListener("keypress",e => {
                    var key = e.key ;
                    if(!key.match(/[0-9.]/))
                        e.preventDefault();
                    if(key=="." && e.target.innerText.includes(".")) {
                        e.preventDefault();
                    }
                })
                newCell.append(valueDiv);
            } else if(i == headerCells.length - 1){
                let deleteRowBtn = document.createElement("div");
                deleteRowBtn.classList.add("delete-row-btn");
                deleteRowBtn.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>ic_close_24px</title>
                    <g>
                        <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
                    </g>
                </svg>` ;
                deleteRowBtn.addEventListener("click",()=>this.deleteRow(newRow));
                newCell.append(deleteRowBtn);
            }

        });
        this.updateSerialNumber();
        return newRow ;
    }

    addField(fieldTitle="",fieldColor="#000000"){
        let index = this.table.tHead.rows[0].cells.length - 1 ;
        // add field in thead
        let newFieldHeader = this.table.tHead.rows[0].insertCell(index);
        let fieldRow = document.createElement("div") ;
        let fieldName = document.createElement("div") ;
        let deleteFieldBtn = document.createElement("div");
        fieldRow.classList.add("field-row");
        fieldName.setAttribute("data-name","field");
        fieldName.contentEditable = true ;
        fieldName.innerText = fieldTitle || "Field" + (index - 1) ;
        deleteFieldBtn.classList.add("delete-field-btn");
        deleteFieldBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>ic_close_24px</title>
            <g>
                <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
            </g>
        </svg>` ;
        deleteFieldBtn.addEventListener("click",()=>this.deleteField(newFieldHeader)); 
        fieldRow.innerHTML = `<div data-name="color"><input type="color" value="${fieldColor}"></div>`;
        fieldRow.append(fieldName);
        fieldRow.append(deleteFieldBtn);
        newFieldHeader.append(fieldRow);
    
        // add values in tbody
        [...this.table.tBodies[0].rows].forEach(row => {
            let newCell = row.insertCell(index);
            let valueDiv = document.createElement("div");
            valueDiv.setAttribute("data-name","value");
            valueDiv.contentEditable = true ;
            valueDiv.addEventListener("keypress",e => {
                var key = e.key ;
                if(!key.match(/[0-9.]/))
                    e.preventDefault();
                if(key=="." && e.target.innerText.includes(".")) {
                    e.preventDefault();
                }
            })
            newCell.append(valueDiv);
        });

        // add empty cells in footer
        this.table.tFoot.rows[0].insertCell(index);

        this.updateFieldNumber()
    }

    deleteRow(row){
        row.remove();
        this.updateSerialNumber();
    }

    deleteField(fieldHeader){
        let index = fieldHeader.getAttribute("data-field-index") ;
        // remove cell from Thead
        this.table.tHead.rows[0].cells[index].remove();
        // remove cell from Tbody
        [...this.table.tBodies[0].rows].forEach(row => {
            row.cells[index].remove();
        })
        // remove cell from TFoot
        this.table.tFoot.rows[0].cells[index].remove();

        this.updateFieldNumber()
    }

    updateSerialNumber(){
        [...this.table.tBodies[0].rows].forEach((row,i) => {
            row.cells[0].innerText = i + 1 ;
        })
    }

    updateFieldNumber(){
        let cells = [...this.table.tHead.rows[0].cells]
        for(let i=2;i<cells.length;i++) {
            cells[i].setAttribute("data-field-index",i);
        }
    }

    getData(){
        let fieldNames =  [...this.table.tHead.rows[0].cells].slice(2,-1).map(e => e.querySelector(`[data-name="field"]`).innerText)  ;
        let fieldColors = [...this.table.tHead.rows[0].cells].slice(2,-1).map(e => e.querySelector(`[data-name="color"] input[type="color"]`).value) 
        let data = [] ;
        [...this.table.tBodies[0].rows].forEach(row => {
            let label = row.querySelector(`[data-name="label"]`).innerText ;
            let values = [...row.cells].slice(2,-1).map(e => e.querySelector(`[data-name="value"]`).innerText)
            
            data.push({
                name  : label ,
                color : fieldColors ,
                value : values ,
                field : fieldNames
            })

        });

        return data ;
    }

    parseArray(str=""){
        str = str.replaceAll("[","");
        str = str.replaceAll("]","");
        str = str.replaceAll(" ","");
        str = str.replaceAll("'","");
        return str.split(",");
    }

    setData(dataSet){
        if(dataSet.length != 0) {
            let fields = this.parseArray(dataSet[0].field);
            let colors = this.parseArray(dataSet[0].color);

            fields.forEach((field,i)=>{
                this.addField(field,colors[i]);
            });

            dataSet.forEach(data => {
                let label = data.name ;
                let value = this.parseArray(data.value);

                let row = this.addRow();
                row.querySelector(`[data-name="label"]`).innerText = label ;
                [...row.querySelectorAll(`[data-name="value"]`)].forEach((valueField,i)=>{
                    valueField.innerText = value[i];
                })
            });
        }
    }
    
}

customElements.define("compound-data-editor",CompoundDataEditor);
