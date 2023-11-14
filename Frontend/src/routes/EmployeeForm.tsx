import { SyntheticEvent, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import {
  Alert,
  Button,
  Container,
  FormControl,
  FormControlLabel,
  FormLabel,
  Input,
  InputLabel,
  MenuItem,
  Select,
  Stack,
  Switch,
  Typography,
} from "@mui/material";

import axios from "../api";
import { Category, Employee } from "../types/types";

interface EmployeeFormProps {
  isEdit?: boolean;
}

export default function EmployeeForm({ isEdit }: EmployeeFormProps) {
  const navigate = useNavigate();

  const { id } = useParams<{ id: string }>();

  useEffect(() => {
    if (!isEdit) return;
    axios.get<{ employees: Employee[] }>("employees").then(function (response) {
      const employees = response.data.employees;
      const employee = employees.find((cat) => {
        return cat.id === parseInt(id ?? "", 10);
      });
      setName(employee?.name ?? "");
      setCPF(employee?.cpf.toString() ?? "");
      setEmail(employee?.email ?? "");
      setStatus(Boolean(employee?.status) ?? true);
    });
  }, [id, isEdit]);


  const [name, setName] = useState("");
  const [cpf, setCPF] = useState("");
  const [email, setEmail] = useState("");
  const [passwd, setPasswd] = useState("");
  const [status, setStatus] = useState(true);
  const [errors, setErrors] = useState<string | null>(null);
  const [success, setSuccess] = useState<boolean | null>(null);

  function handleSubmit(e: SyntheticEvent<HTMLFormElement, SubmitEvent>) {
    // Prevent the browser from reloading the page
    e.preventDefault();

    const params = { name, cpf, email,passwd, status };
    const axiosRequest = isEdit
      ? axios.put(`employees/${id}`, params)
      : axios.post("employees/", params);

    axiosRequest
      .then(function () {
        setSuccess(true);
        setTimeout(() => {
          navigate("/employee/list");
        }, 3000);
      })
      .catch(function (error) {
        setErrors(error.response.data.message);
      });
  }

  return (
    <Container>
      <Typography variant="h2">Employee</Typography>
      {errors ? <Alert severity="error">{errors}</Alert> : null}
      {success ? (
        <Alert severity="success">Employee successfully saved</Alert>
      ) : null}

      <form method="POST" onSubmit={handleSubmit}>
        <Stack spacing={2} alignItems="center">
          <FormControl>
            <FormLabel>Name:</FormLabel>
            <Input
              type="text"
              name="name"
              value={name}
              onChange={(e) => {
                setName(e.target.value);
              }}
              required
            />
          </FormControl>
          <FormControl>
            <FormLabel>CPF:</FormLabel>
            <Input
              type="text"
              name="cpf"
              value={cpf}
              onChange={(e) => {
                setCPF(e.target.value);
              }}
            />
          </FormControl>
          <FormControl>
            <FormLabel>Email:</FormLabel>
            <Input
              type="text"
              name="email"
              value={email}
              onChange={(e) => {
                setEmail(e.target.value);
              }}
            />
          </FormControl><FormControl>
            <FormLabel>Password:</FormLabel>
            <Input
              type="text"
              name="email"
              value={passwd}
              onChange={(e) => {
                setPasswd(e.target.value);
              }}
            />
          </FormControl>
          <FormControl>
            <FormLabel>Status:</FormLabel>
            <FormControlLabel
              control={
                <Switch
                  checked={status}
                  onChange={() => {
                    setStatus(!status);
                  }}
                />
              }
              label={status ? "Enable" : "Disable"}
            />
          </FormControl>

          <Button type="submit" variant="contained" color="secondary">
            Send
          </Button>
        </Stack>
      </form>
    </Container>
  );
}
