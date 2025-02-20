---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/variables-packer-hashi-corp-developer/","tags":["rw/articles"]}
---

![rw-book-cover](https://developer.hashicorp.com/og-image/packer.jpg)

In the previous tutorial, you implemented your first provisioner. However, your Packer template is static. Currently if you want to change the contents of the file, you need to manually update your template.

You can use input variables to serve as parameters for a Packer build, allowing aspects of the build to be customized without altering Packer template. In addition, Packer variables are useful when you want to reference a specific value throughout your template.

In this tutorial, you will add Packer variables to parameterize your Packer build, making it more robust.

This tutorial assumes that you are continuing from the previous tutorials. If not, follow the steps below before continuing.

* Create a directory named `packer_tutorial` and paste the following configuration into a file named `docker-ubuntu.pkr.hcl`.

```
    docker = {
      version = ">= 1.0.8"
      source = "github.com/hashicorp/docker"

  image  = "ubuntu:jammy"
  commit = true

  name    = "learn-packer"
  sources = [

    environment_vars = [
    inline = [

    inline = ["echo This provisioner runs last"]

```

Once you have successfully initialized the template, you can continue with the rest of this tutorial.

Add the following variable block to your `docker-ubuntu.pkr.hcl` file.

Variable blocks declare the variable name (`docker_image`), the data type (`string`), and the default value (`ubuntu:jammy`). While the variable type and default values are optional, we recommend you define these attributes when creating new variables.

Treat Packer variables as constants — you cannot update them during run time.

In your Packer template, update your source block to reference the `docker_image` variable. Notice how the template references the variable as `var.docker_image`.

Update the second provisioner to print the `docker_image` variable. Notice that even though the `docker_image` variable was used directly in the source block above, to embed a variable in another string you need to template it using the syntax `${}`, as shown when echoing `docker_image` in the provisioner block.

Build the image.

```
    learn-packer.docker.ubuntu: Run command: docker run -v /Users/youruser/.packer.d/tmp176397065:/packer-files -d -i -t --entrypoint=/bin/sh -- ubuntu:jammy
==> learn-packer.docker.ubuntu: Provisioning with shell script: /var/folders/s6/m22_k3p11z104k2vx1jkqr2c0000gp/T/packer-shell863456722
==> learn-packer.docker.ubuntu: Provisioning with shell script: /var/folders/s6/m22_k3p11z104k2vx1jkqr2c0000gp/T/packer-shell703813640

--> learn-packer.docker.ubuntu: Imported Docker image: sha256:e3aafb04d8d628514370617bdf949e9d5e2f0109cb92be63d230be63420e2811

```

The output is the same as before, but now the `docker_image` variable is being used to specify that the `"ubuntu:jammy"` base image should be used.

You'll know it worked if you see the `Builds finished. The artifacts of successful builds...` message near the bottom.

Since `docker_image` is parameterized, you can define your variable before building the image. There are multiple ways to [assign variables](https://developer.hashicorp.com/packer/guides/hcl/variables#assigning-variables). The order of ascending precedence is: variable defaults, environment variables, variable file(s), command-line flag. In this section, you will define variables using variable files and command-line flags.

Create a file named `example.pkrvars.hcl`.

Add the following snippet into it.

Build the image with the `--var-file` flag.

```
==> learn-packer.docker.ubuntu: Provisioning with shell script: /var/folders/s6/m22_k3p11z104k2vx1jkqr2c0000gp/T/packer-shell905783662

```

Notice how the build step runs the `ubuntu:lunar` Docker image, the value for `docker_image` defined by the variable file.

Packer will automatically load any variable file that matches the name `*.auto.pkrvars.hcl`, without the need to pass the file via the command line.

Rename your variable file so Packer automatically loads it.

```
$ mv example.pkrvars.hcl example.auto.pkrvars.hcl

```

Build the image and notice the Docker image running `ubuntu:lunar`. The `packer build .` command loads all the contents in the current directory.

Build the image, setting the variable directly from the command line.

```
==> learn-packer.docker.ubuntu: Provisioning with shell script: /var/folders/s6/m22_k3p11z104k2vx1jkqr2c0000gp/T/packer-shell930656710

```

Notice how the build step runs the `ubuntu:focal` Docker image, the value for `docker_image` defined by the command-line flag. The command-line flag has the highest precedence and will override values defined by other methods.

In this tutorial, you made your Packer template more robust by parameterizing it with variables. Then, you defined your variables using variable files and command-line flags during the build step, learning variable definition order of precedence in the process. Continue to the [next tutorial](https://developer.hashicorp.com/packer/tutorials/docker-get-started/docker-get-started-parallel-builds) to create multiple images in parallel using the same template.

Refer to the following resources for additional details on the concepts covered in this tutorial:
