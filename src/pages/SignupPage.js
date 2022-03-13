import "./LoginSignup.css";
import { Grid } from "@mui/material";
import Signup from "../auth/Signup";
import login from "../assets/login.svg";

export default function SignupPage() {
  return (
    <>
      <Grid container direction="row">
        <Grid item sm={6} md={3} className="rightt-box">
          <Grid
            item
            display="flex"
            justifyContent="flex-end"
            alignItems="flex-end"
          >
            <img
              src={login}
              alter="hello"
              style={{ width: "500px", height: "500px" }}
            />
          </Grid>
        </Grid>
        <Grid item sm={6} md={6} className="leftt-box">
          <div className="box">
            <Signup />
          </div>
        </Grid>
      </Grid>
    </>
  );
}
