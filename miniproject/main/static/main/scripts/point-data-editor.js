
class PointDataEditor extends HTMLElement {
    constructor() {
        super();
        this.createEditor();
    }

    createEditor() {
        this.tableWrapper = document.createElement("div");
        this.table = document.createElement("table");

        this.table.classList.add("no-hiding");
        this.table.classList.add("no-padding");
        this.table.classList.add("line-data-editor");

        this.tableWrapper.classList.add("table-wrapper");

        this.tableWrapper.append(this.table);
        this.append(this.tableWrapper);
        this.table.createTBody();

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
        addRowBtn.addEventListener("click", () => this.addRow());

        let addFieldBtn = document.createElement("div");
        addFieldBtn.classList.add("add-field-btn");
        addFieldBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>ic_add_24px</title>
            <g>
                <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path>
            </g>
        </svg>
        ` ;
        addFieldBtn.addEventListener("click", () => this.addField());

        // add basic template
        this.header = this.table.createTHead();
        let headerRow = this.header.insertRow();
        headerRow.insertCell(-1).innerHTML = "#";
        headerRow.insertCell(-1).append(addFieldBtn);

        this.footer = this.table.createTFoot();
        let footerRow = this.footer.insertRow();
        footerRow.insertCell(-1);
        let btnCell = footerRow.insertCell(-1)
        btnCell.setAttribute("colspan", "2");
        btnCell.append(addRowBtn);

        this.addField();

    }

    addRow() {
        let newRow = this.table.tBodies[0].insertRow(-1);
        let headerCells = [...this.table.tHead.rows[0].cells];
        headerCells.forEach((cell, i) => {
            if (i == 0) {
                newRow.insertCell(-1);
            } if (i >= 1 && i != headerCells.length - 1) {
                let newCellx = newRow.insertCell(-1);
                let newCelly = newRow.insertCell(-1);

                for (var k = 0; k < 2; k++) {
                    let valueDiv = document.createElement("div");
                    valueDiv.setAttribute("data-name", "value");
                    valueDiv.contentEditable = true;
                    valueDiv.addEventListener("keypress", e => {
                        var key = e.key;
                        if (!key.match(/[0-9.]/))
                            e.preventDefault();
                        if (key == "." && e.target.innerText.includes(".")) {
                            e.preventDefault();
                        }
                    })
                    if (k == 0) {
                        valueDiv.setAttribute("data-axis", "x");
                        newCellx.append(valueDiv);
                    } else {
                        valueDiv.setAttribute("data-axis", "y");
                        newCelly.append(valueDiv);
                    }
                }
            } else if (i == headerCells.length - 1) {
                let newCell = newRow.insertCell(-1);;
                let deleteRowBtn = document.createElement("div");
                deleteRowBtn.classList.add("delete-row-btn");
                deleteRowBtn.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>ic_close_24px</title>
                    <g>
                        <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
                    </g>
                </svg>` ;
                deleteRowBtn.addEventListener("click", () => this.deleteRow(newRow));
                newCell.append(deleteRowBtn);
            }

        });
        this.updateSerialNumber();
        return newRow;
    }

    addField(fieldTitle = "", fieldColor = "#000000") {
        let index = this.table.tHead.rows[0].cells.length - 1;
        // add field in thead
        let newFieldHeader = this.table.tHead.rows[0].insertCell(index);
        let fieldRow = document.createElement("div");
        let fieldName = document.createElement("div");
        let deleteFieldBtn = document.createElement("div");
        newFieldHeader.setAttribute("colspan", "2");
        fieldRow.classList.add("field-row");
        fieldName.setAttribute("data-name", "field");
        fieldName.contentEditable = true;
        fieldName.innerText = fieldTitle || "Field" + (index);
        deleteFieldBtn.classList.add("delete-field-btn");
        deleteFieldBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>ic_close_24px</title>
            <g>
                <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
            </g>
        </svg>` ;
        deleteFieldBtn.addEventListener("click", () => this.deleteField(newFieldHeader));
        fieldRow.innerHTML = `<div data-name="color"><input type="color" value="${fieldColor}"></div>`;
        fieldRow.append(fieldName);
        fieldRow.append(deleteFieldBtn);
        newFieldHeader.append(fieldRow);

        // add values in tbody
        [...this.table.tBodies[0].rows].forEach(row => {

            let newCellx = row.insertCell(row.cells.length - 1);
            let newCelly = row.insertCell(row.cells.length - 1);

            for (var k = 0; k < 2; k++) {
                let valueDiv = document.createElement("div");
                valueDiv.setAttribute("data-name", "value");
                valueDiv.contentEditable = true;
                valueDiv.addEventListener("keypress", e => {
                    var key = e.key;
                    if (!key.match(/[0-9.]/))
                        e.preventDefault();
                    if (key == "." && e.target.innerText.includes(".")) {
                        e.preventDefault();
                    }
                })
                if (k == 0) {
                    valueDiv.setAttribute("data-axis", "x");
                    newCellx.append(valueDiv);
                } else {
                    valueDiv.setAttribute("data-axis", "y");
                    newCelly.append(valueDiv);
                }
            }
        });

        // add empty cells in footer
        this.table.tFoot.rows[0].insertCell(index + 1);
        this.table.tFoot.rows[0].insertCell(index + 1);

        this.updateFieldNumber()
    }

    deleteRow(row) {
        row.remove();
        this.updateSerialNumber();
    }

    deleteField(fieldHeader) {
        if (this.table.tHead.rows[0].cells.length == 3) {
            return;
        }
        let index = parseInt(fieldHeader.getAttribute("data-field-index"));

        // remove cell from Thead
        this.table.tHead.rows[0].cells[index].remove();

        // remove cell from Tbody
        [...this.table.tBodies[0].rows].forEach(row => {
            row.deleteCell(2 * index - 1);
            row.deleteCell(2 * index - 1);
        })

        // remove cell from TFoot
        this.table.tFoot.rows[0].cells[this.table.tFoot.rows[0].cells.length - 1].remove();

        this.updateFieldNumber()
    }

    updateSerialNumber() {
        [...this.table.tBodies[0].rows].forEach((row, i) => {
            row.cells[0].innerText = i + 1;
        })
    }

    updateFieldNumber() {
        let cells = [...this.table.tHead.rows[0].cells]
        for (let i = 1; i < cells.length - 1; i++) {
            cells[i].setAttribute("data-field-index", i);
        }
    }

    getData() {
        let fieldNames = [...this.table.tHead.rows[0].cells].slice(1, -1).map(e => e.querySelector(`[data-name="field"]`).innerText);
        let fieldColors = [...this.table.tHead.rows[0].cells].slice(1, -1).map(e => e.querySelector(`[data-name="color"] input[type="color"]`).value)

        let data = [];
        for (let i = 1; i < this.table.tHead.rows[0].cells.length - 1; i++) {
            let values = [];
            [...this.table.tBodies[0].rows].forEach((row, r) => {

                let x = row.cells[2 * i - 1].querySelector("[data-name='value']").innerText || "0";
                let y = row.cells[2 * i].querySelector("[data-name='value']").innerText || "0";

                values.push([x, y]);

            });

            data.push({
                name: fieldNames[i - 1],
                color: fieldColors[i - 1],
                value: values,
                field: ""
            })
        }

        return data;
    }

    parseArray(str = "") {
        str = str.replaceAll("[", "");
        str = str.replaceAll("]", "");
        str = str.replaceAll(" ", "");
        str = str.replaceAll("'", "");
        return str.split(",");
    }

    setData(dataSet) {
        let fieldInfo = [];
        dataSet.forEach((data, i) => {
            fieldInfo.push({
                name: data.name,
                color: data.color
            });

            if (i != 0)
                this.addField();
        });

        // set fields
        [...this.table.tHead.rows[0].cells].slice(1, -1).forEach((field, i) => {
            field.querySelector(`[data-name="field"]`).innerText = fieldInfo[i].name;
            field.querySelector(`[data-name="color"] input[type="color"]`).value = fieldInfo[i].color
        })

        let valueRow = [];

        // set data
        dataSet.forEach((data, i) => {
            let value = this.parseArray(data.value);
            let rowCount = Math.ceil(value.length / 2);

            for (let r = 0; r < rowCount; r++) {
                valueRow[r] = valueRow[r] || [];
                valueRow[r].push(value[2 * r]);
                valueRow[r].push(value[2 * r + 1]);
            }



        });

        valueRow.forEach(value => {
            let row = this.addRow();
            [...row.querySelectorAll(`[data-name="value"]`)].forEach((valueField, i) => {
                valueField.innerText = value[i];
            })
        })
    }

}

customElements.define("point-data-editor", PointDataEditor);
