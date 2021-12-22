import React, { useState, useEffect } from 'react';
import { forwardRef } from 'react';
import MaterialTable from "material-table";
import Search from "@material-ui/icons/Search";
import FilterList from '@material-ui/icons/FilterList';
import SaveAlt from '@material-ui/icons/SaveAlt';
import FirstPage from '@material-ui/icons/FirstPage';
import LastPage from '@material-ui/icons/LastPage';
import ChevronRight from '@material-ui/icons/ChevronRight';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import Clear from '@material-ui/icons/Clear';
import ArrowDownward from '@material-ui/icons/ArrowDownward';
import Edit from '@material-ui/icons/Edit';
import DeleteOutline from '@material-ui/icons/DeleteOutline';
import AddBox from '@material-ui/icons/AddBox';
import Remove from '@material-ui/icons/Remove';
import Check from '@material-ui/icons/Check';
import './App.css';

function App() {
  const tableIcons = {
    Search: forwardRef((props, ref) => <Search {...props} ref={ref} />),
    Filter: forwardRef((props, ref) => <FilterList {...props} ref={ref} />),
    Export: forwardRef((props, ref) => <SaveAlt {...props} ref={ref} />),
    FirstPage: forwardRef((props, ref) => <FirstPage {...props} ref={ref} />),
    LastPage: forwardRef((props, ref) => <LastPage {...props} ref={ref} />),
    NextPage: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
    PreviousPage: forwardRef((props, ref) => <ChevronLeft {...props} ref={ref} />),
    ResetSearch: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
    SortArrow: forwardRef((props, ref) => <ArrowDownward {...props} ref={ref} />),
    Edit: forwardRef((props, ref) => <Edit {...props} ref={ref} />),
    Delete: forwardRef((props, ref) => <DeleteOutline {...props} ref={ref} />),
    Add: forwardRef((props, ref) => <AddBox {...props} ref={ref} />),
    ThirdStateCheck: forwardRef((props, ref) => <Remove {...props} ref={ref} />),
    Check: forwardRef((props, ref) => <Check {...props} ref={ref} />),
    Clear: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
  };

  const [customerData, setCustomerData] = useState([]);

  useEffect(() => {
    fetch('/customers').then(res => res.json()).then(data => {
      setCustomerData(data);
    });
  }, []);

  return (
    <div className="App">
      <div className="containers">
      </div>
      <MaterialTable
        title={<h1 id='mt-title-h1'> Customers Data </h1>}
        data={customerData.data}
        columns={[
          { title: 'Id', field: 'id', type: 'numeric', editable: 'never' },
          { title: 'Name', field: 'name' },
          { title: 'Birthdate', field: 'birthdate' },
          { title: 'Sex', field: 'sex' },
          { title: 'Address', field: 'address' },
          { title: 'Residence', field: 'residence' },
          { title: 'Phone', field: 'phone_number' },
          { title: 'Mail', field: 'mail' },
          { title: 'SSN', field: 'ssn' },
          { title: 'Job', field: 'job' },
          { title: 'Company', field: 'company' },
        ]}
        editable={{
          // adding new customer data
          onRowAdd: newData =>
            new Promise((resolve, reject) => {
              setTimeout(() => {
                console.log(newData);
                fetch(
                  `/customers`,
                   {
                     method: 'POST',
                     body: JSON.stringify(newData)
                   }
                );
                window.location.reload(false);

                resolve();
              }, 1000)
            }),
          // update the customers data
          onRowUpdate: (newData, oldData) =>
            new Promise((resolve, reject) => {
              setTimeout(() => {
                console.log(newData.id);
                console.log(newData);
                fetch(
                  `/customers/${oldData.id}`,
                   {
                     method: 'PUT',
                     body: JSON.stringify(newData)
                   }
                );
                window.location.reload(false);
                resolve();
              }, 1000)
            }),
          // Delete customers data
          onRowDelete: oldData =>
            new Promise((resolve, reject) => {
              setTimeout(() => {
                console.log(oldData.id);
                console.log(`/customers/${oldData.id}`);
                fetch(`/customers/${oldData.id}`, {method: 'DELETE'});
                window.location.reload(false);
                resolve()
              }, 1000)
            }),
        }}
        options={{
          search: true,
          paging: true,
          filtering: true,
          exportButton: true,
          //  selection: true,
          headerStyle: {backgroundColor: 'orange', fontSize: 16, fontWeight: 'bold', position: 'sticky'},
        }}
        icons={tableIcons}
        style={{
          marginLeft: '3vw',
          marginRight: '3vw',
          marginTop: '2vh',
          marginBottom: '2vh',
          backgroundColor: 'powderblue',
          padding: 1,
        }}
      />
    </div>
  );
}

export default App;
